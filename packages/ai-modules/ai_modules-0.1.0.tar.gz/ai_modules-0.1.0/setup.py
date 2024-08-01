# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-modules",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A flexible and extensible framework for managing and processing various types of data objects using AI techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cdaprod/AI-Modules",
    packages=find_packages(where="app"),
    package_dir={"": "app"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.68.0,<0.69.0",
        "pydantic>=1.8.0,<2.0.0",
        "uvicorn>=0.15.0,<0.16.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.4,<7.0.0",
            "pytest-cov>=2.12.0,<3.0.0",
            "flake8>=3.9.2,<4.0.0",
            "black>=21.5b1,<22.0",
        ],
    },
)