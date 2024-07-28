from setuptools import setup, find_packages
from setuptools_rust import RustExtension

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rustytable",
    version="0.1.1",
    author="Jahidul Hasan Hemal",
    author_email="jahidulhasanhemal@gmail.com",
    description="A high-performance, feature-rich table formatting library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhhemal/rustytable",
    packages=find_packages(),
    rust_extensions=[RustExtension("rustytable.rustytable", "Cargo.toml", binding="pyo3")],
    install_requires=[
        # Add any Python dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Rust",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
    zip_safe=False,
)
