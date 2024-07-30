from __future__ import print_function
from setuptools import setup
import codecs
import os
import re


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), "r").read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="envparse2",
    version=find_version(".", "envparse2.py"),
    url="https://github.com/beregond/envparse2",
    license="MIT",
    author="Rick Harris",
    author_email="rconradharris@gmail.com",
    tests_require=["pytest"],
    description="Simple environment variable parsing",
    long_description=read("README.rst"),
    py_modules=["envparse2"],
    platforms="any",
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
