from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()
requirements = [x.strip() for x in requirements]


setup(name='snake',
    description="A python version of the nostalgic nokia game snake",
    packages=find_packages(),
    install_requires=requirements)
#
