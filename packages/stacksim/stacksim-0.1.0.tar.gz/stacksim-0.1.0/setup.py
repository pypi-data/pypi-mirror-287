from setuptools import find_packages, setup
import os
__version__ = "0.1.0"

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='stacksim',
    version="0.1.0",
    description='Stack Visualization Tool',
    long_description=long_description,
    packages=find_packages(),
    package_dir={
        "stacksim": "stacksim"
    },
    include_package_data=True,
    package_data={
        'stacksim': ['templates/*.html'],
    },
    scripts=["stacksim/stacksim"], 
    install_requires = ["prompt_toolkit", "Sphinx", "termcolor", "ansi2html"],
    entry_points = {
        'spinx.extension': [ 'stack = stacksim.stackDirective' ]
    }
)
