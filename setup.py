from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="gcodeBuddy",
    version="0.2.2",
    description="Python package used to write to, read from, and interpret g-code files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gcodeBuddy.readthedocs.io/",
    author="Spencer Bertram",
    author_email="spenbert02@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["gcodeBuddy"],
    include_package_data=True,
    install_requires=["bs4", "matplotlib", "numpy"]
)