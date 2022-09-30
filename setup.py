#!-*- coding: utf-8 -*-

import os

import ffprog
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()

setup(
    name="ffprog",
    version=thresh.__version__,
    description="progress bar for ffmpeg",
    long_description=README,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author=["Cooper"],
    author_email=["mike@hotmail.com"],
    url="not yet darling",
    keywords=["ffmpeg", "progress bar", "commandline ui"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    scripts=["ffprog/ffprog", "ffprog/ffprog"],
)
