from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = "A basic hello pkg"

setup(
    name = "okela",
    version=VERSION,
    author="okela",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['python','hello'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)