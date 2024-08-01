import os
from typing import Callable, Any
import asyncio
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
import tempfile

class BackpropAPI:
    def __init__(self):
        self.token = os.getenv("BP_TOKEN")
        self.api_key_header = APIKeyHeader(name="Authorization", auto_error=False)
        self.dependency_funcs = []
        self.ready = asyncio.Event()
        
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup
            for func in self.dependency_funcs:
                await func()
            self.ready.set()
            yield
            # Shutdown
            # Add any cleanup code here if needed

        self.app = FastAPI(lifespan=lifespan)

        # Setup CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allows all origins
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods
            allow_headers=["*"],  # Allows all headers
        )

        @self.app.get("/health")
        async def health_check():
            return {"status": "ok"}

        @self.app.get("/ready")
        async def ready_check():
            if self.ready.is_set():
                return {"status": "ready"}
            raise HTTPException(status_code=503, detail="Dependencies not loaded")

    def load_dependency(self):
        def decorator(func: Callable[[], Any]):
            self.dependency_funcs.append(func)
            return func
        return decorator

    def endpoint(self, path: str):
        def decorator(func: Callable[[Any], Any]):
            @self.app.post(path)
            async def wrapper(request: Request, api_key: str = Depends(self.api_key_header)):
                if self.token and api_key != f"Bearer {self.token}":
                    raise HTTPException(status_code=403, detail="Could not validate credentials")
                
                await self.ready.wait()
                
                body = await request.json()
                result = await func(body)
                return result
            return wrapper
        return decorator

    def generate_self_signed_cert(self, common_name: str = "localhost"):
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Organization"),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ])
        
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.utcnow()
        ).not_valid_after(
            datetime.utcnow() + timedelta(days=365)
        ).add_extension(
            x509.SubjectAlternativeName([x509.DNSName(common_name)]),
            critical=False,
        ).sign(key, hashes.SHA256())
        
        cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
        key_pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        return cert_pem, key_pem

    def get_app(self):
        return self.app

    def serve(self, host="0.0.0.0", port=8000):
        app = self.get_app()
        use_https = os.getenv("BP_USE_HTTPS", "").lower() == "true"
        SSL_CERT = os.getenv("BP_SSL_CERT")
        SSL_KEY = os.getenv("BP_SSL_KEY")
        
        if use_https:
            if SSL_CERT and SSL_KEY:
                # Use provided SSL certificate and key
                temp_cert_file = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
                temp_key_file = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
                
                temp_cert_file.write(SSL_CERT.encode())
                temp_key_file.write(SSL_KEY.encode())
                
                temp_cert_file.close()
                temp_key_file.close()
                
                ssl_config = {
                    "ssl_keyfile": temp_key_file.name,
                    "ssl_certfile": temp_cert_file.name,
                }
            else:
                # Generate self-signed certificate
                cert_pem, key_pem = self.generate_self_signed_cert()
                
                temp_cert_file = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
                temp_key_file = tempfile.NamedTemporaryFile(delete=False, mode='w+b')
                
                temp_cert_file.write(cert_pem)
                temp_key_file.write(key_pem)
                
                temp_cert_file.close()
                temp_key_file.close()
                
                ssl_config = {
                    "ssl_keyfile": temp_key_file.name,
                    "ssl_certfile": temp_cert_file.name,
                }
                uvicorn.run(app, host=host, port=port, **ssl_config)
        else:
            uvicorn.run(app, host=host, port=port)

    def __setattr__(self, name, value):
        self.__dict__[name] = value
