# setup.py

from setuptools import setup, find_packages

setup(
    name="vjwhats",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
    ],
    description="A Python library to interact with WhatsApp Web using Selenium.",
    author="Fioruci",
    author_email="notfryska@gmail.com",
    url="https://github.com/Fioruci/vjwhats",
)
