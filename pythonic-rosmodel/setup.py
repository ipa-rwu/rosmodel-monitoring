#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="pythonic_rosmodel",
    version="0.0.1",
    description="pythonic rosmodel metamodel and syntax",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pyecore", "textx", "textx-pyecoregen", "autopep8"],
    license="Apache License, Version 2.0",
    python_requires=">=3.6",
    entry_points={'console_scripts': [
        'pyecoregen = pythonic_rosmodel.cli:main']},
)
