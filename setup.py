#!/usr/bin/env python

"""The setup script."""

import pathlib

from pkg_resources import parse_requirements
from setuptools import find_packages, setup


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

with open("requirements.txt") as requirements_file:
    requirements = [
        str(req) for req in parse_requirements(requirements_file.readlines())
    ]

setup(
    name="cnab",
    version="0.0.1",
    description="A Python implementation of the CNAB240 file to perform bulk payments.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vintasoftware/vinta-pagamentos",
    author="Rebeca Sarai (Vinta Software)",
    author_email="rebeca@vinta.com.br",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 -  Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Bank Payments :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="cnab240, payments, openbank",
    install_requires=requirements,
    license="MIT license",
    packages=find_packages(include="vinta-pagamentos"),
    entry_points={  # Optional
        "console_scripts": [
            "sample=sample:main",
        ],
    },
)
