import os
import uvicorn

def serve(api, host="0.0.0.0", port=8000):
    app = api.get_app()
    use_https = os.getenv("BACKPROP_USE_HTTPS", "").lower() == "true"
    
    if use_https:
        ssl_keyfile = os.getenv("BACKPROP_SSL_KEY")
        ssl_certfile = os.getenv("BACKPROP_SSL_CERT")
        if not ssl_keyfile or not ssl_certfile:
            raise ValueError("BACKPROP_SSL_KEY and BACKPROP_SSL_CERT must be set when BACKPROP_USE_HTTPS is true")
        uvicorn.run(app, host=host, port=port, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)
    else:
        uvicorn.run(app, host=host, port=port)
