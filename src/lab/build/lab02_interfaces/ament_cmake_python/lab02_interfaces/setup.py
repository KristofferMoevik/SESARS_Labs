from setuptools import find_packages
from setuptools import setup

setup(
    name='lab02_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('lab02_interfaces', 'lab02_interfaces.*')),
)
