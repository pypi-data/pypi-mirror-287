from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)

setup(name='PostgreSQL-connector-python', #package name
      version='1.0.0',
      description='White Hat Researcher',
      author='Pastaga',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
