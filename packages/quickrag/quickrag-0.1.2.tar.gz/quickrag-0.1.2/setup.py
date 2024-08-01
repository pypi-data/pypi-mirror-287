from setuptools import setup, find_packages

setup(
    name="quickrag",
    version="0.1.2",
    author="Vansh Kharidia",
    author_email="vanshkharidia7@gmail.com",
    description="A Quick Retrieval-Augmented Generation (RAG) system using transformers.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VanshK7/quickrag",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "torch>=1.9.0",
        "numpy>=1.19.2",
        "pandas>=1.1.3",
        "tqdm>=4.62.3",
        "sentence-transformers>=2.1.0",
        "transformers>=4.10.0",
        "PyMuPDF>=1.19.0",
        "spacy>=3.1.2",
        "textwrap3>=0.9.2"
    ],
)
