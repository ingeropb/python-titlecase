import os
import sys

from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

from titlecase import __version__

setup(name='titlecase',
    version=__version__,
    description="Python Port of John Gruber's titlecase.pl, forked from Pat Pannuto",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Text Processing :: Filters",
    ],
    keywords='string formatting',
    author="Inger Klekacz, Pat Pannuto, Stuart Colville, John Gruber",
    author_email="iklekacz@opb.org",
    url="https://github.com/ingeropb/python-titlecase",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    tests_require=['nose'],
    setup_requires=['nose>=1.0'],
    test_suite="titlecase.tests",
    entry_points = """\
    """
)

