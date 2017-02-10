import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "myCustomLog",
    version = "0.1.0",
    author = "Bankde",
    author_email = "Bankde@hotmail.com",
    description = ("A simple stupid wrapper class of python logger."),
    license = "BSD",
    keywords = "python logger wrapper fbchat easy",
    url = "https://github.com/Bankde/myCustomLog",
    packages=['myCustomLog'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
