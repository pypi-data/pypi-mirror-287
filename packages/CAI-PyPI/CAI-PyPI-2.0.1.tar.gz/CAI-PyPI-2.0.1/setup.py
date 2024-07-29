#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup script for CAI-PyPI package."""

from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get requirements
with open("requirements.txt", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="CAI-PyPI",
    version="2.0.1",  # Updated version number
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="Python implementation of codon adaptation index, updated for PyPI compatibility",
    long_description=f"CAI-PyPI: An updated version of the Codon Adaptation Index (CAI) package\n\n"
                     f"This package is based on the original CAI project by Benjamin Lee "
                     f"(https://github.com/Benjamin-Lee/CodonAdaptationIndex). It has been updated "
                     f"to resolve compatibility issues with PyPI and ensure the latest version "
                     f"is easily accessible via pip. While maintaining the core functionality of "
                     f"the original project, this version aims to provide a smoother installation "
                     f"process and better integration with PyPI.\n\n"
                     f"Original README:\n\n{long_description}",
    long_description_content_type="text/markdown",
    author="Adibvafa Fallahpour",
    author_email="Adibvafafallahpour@gmail.com",
    url="https://github.com/Adibvafa/CodonAdaptationIndex",
    install_requires=install_requires,
    license="MIT",
    python_requires=">=3.7",
    entry_points={"console_scripts": ["CAI-PyPI=CAI.cli:cli"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="bioinformatics codon adaptation index genetics PyPI",
    project_urls={
        "Bug Reports": "https://github.com/Adibvafa/CodonAdaptationIndex/issues",
        "Source": "https://github.com/Adibvafa/CodonAdaptationIndex",
        "Original Project": "https://github.com/Benjamin-Lee/CodonAdaptationIndex",
    },
)