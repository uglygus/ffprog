#!-*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

README = open(os.path.join(here, "README.md")).read()

with open(os.path.join(here, "VERSION")) as version_file:
    VERSION = version_file.read().strip()


setup(
    name="ffprog",
    version=VERSION,  # ffprog.__version__,  # "0.0.3",
    description="progress bar for ffmpeg",
    long_description=README,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author=["uglygus"],
    author_email=["mike@hotmail.com"],
    url="not yet darling",
    keywords=["ffmpeg", "progress bar", "commandline ui"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": [
            "ffprog=ffprog:ffrun",
        ],
    },
)
