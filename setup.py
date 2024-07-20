from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cland",
    version="0.1.0",
    author="Prathit Joshi",
    author_email="prathit3.14@gmail.com",
    description="A comprehensive toolkit for building Retrieval-Augmented Generation (RAG) systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prathit-tech/cland",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "fastembed",
        "transformers",
        "openai",
        "google-generativeai",
        "qdrant-client",
        "pinecone-client",
        "faiss-cpu",
        "pypdf",
        "beautifulsoup4",
        "requests",
    ],
    extras_require={
        "dev": ["pytest", "black", "isort", "mypy", "flake8"],
    },
)