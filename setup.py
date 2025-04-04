from setuptools import setup, find_packages

# Leer la versión desde version.py
version = {}
with open("fastapi_response_standard/version.py") as f:
    exec(f.read(), version)

setup(
    name="fastapi_response_standard",
    version=version["__version__"],
    description="Estándar de manejo de respuestas y errores para FastAPI",
    author="Stefan Rivera",
    author_email="info@stefanrivera.com",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100",
        "starlette>=0.27",
        "python-jose[cryptography]>=3.3.0"
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.8',
)
