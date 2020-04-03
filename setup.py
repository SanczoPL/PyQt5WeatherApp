import os
import setuptools
import distutils.sysconfig
import os
import sys

NAME = "weather_app"
DESCRIPTION = "test"
AUTHOR = "test"
AUTHOR_EMAIL = "test"
CLASSIFIERS = ["Beta", "Programming Language :: Python :: 3.8"]
PACKAGES = setuptools.find_packages(exclude=["tests*"])
LICENSE = ""

# Read requirements from requirement file
INSTALL_REQUIRES = []
with open("requirements.txt") as f:
	LINES = f.readlines()
	for line in LINES:
		INSTALL_REQUIRES.append(line.rstrip())

# Define additional data


SITE_PACKAGES = distutils.sysconfig.get_python_lib().split(sys.prefix + os.sep)[1].replace("Lib", "lib")

# Version data
PYTHON_REQUIRES = "==3.8.*"
VERSION = "0.0"

setuptools.setup(name=NAME, version=VERSION, description=DESCRIPTION, classifiers=CLASSIFIERS,
                 packages=PACKAGES, install_requires=INSTALL_REQUIRES, include_package_data=True,
                 python_requires=PYTHON_REQUIRES, license=LICENSE)