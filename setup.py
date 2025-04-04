from setuptools import setup, find_packages
import os

# Leer la versión de version.py
version = {}
version_file = ("version.py")
with open(version_file, "r") as f:
    exec(f.read(), version)

setup(
    name="fastapi_response_standard",
    version=version["__version__"],
    description="Estándar reutilizable para manejo de errores y respuestas en FastAPI",
    author="Stefan Rivera",
    author_email="info@stefanrivera.com",
    url="https://github.com/ciskosv/fastapi_response_standard",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.95",
        "starlette>=0.27",
        "python-jose[cryptography]>=3.3.0"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Framework :: FastAPI",
    ],
    python_requires=">=3.8",
)
