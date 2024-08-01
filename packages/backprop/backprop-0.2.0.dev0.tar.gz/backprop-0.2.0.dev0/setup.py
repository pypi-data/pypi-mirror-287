import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backprop",
    version="0.2.0dev0",
    author="Backprop",
    author_email="hello@backprop.co",
    description="A package for easily creating and hosting AI model APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/backprop-ai/backprop",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-multipart",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "backprop=backprop.cli:cli",
        ],
    },
)
