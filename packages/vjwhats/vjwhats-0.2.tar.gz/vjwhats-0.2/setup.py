# setup.py

from setuptools import setup, find_packages

setup(
    name="vjwhats",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "selenium",
    ],
    description="A Python library to interact with WhatsApp Web using Selenium.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Fioruci",
    author_email="notfryska@gmail.com",
    url="https://github.com/Fioruci/vjwhats",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
