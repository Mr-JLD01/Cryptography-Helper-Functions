# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="cryptography-helper-functions",
    version="1.0",
    description="Functions to ease in solving Cryptohack challenges and possibly other cryptography CTF challenges",
    url="https://github.com/Mr-JLD01/Cryptography-Helper-Functions",
    author="John Luke Deny",
    author_email="jldenny0207@aol.com",
    license="MIT",
    packages=find_packages(),
    py_modules=["CryptographyHelperFunctions"],
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Python3",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)