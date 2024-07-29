import os
from setuptools import setup, find_namespace_packages

setup(
    name='zyjared-color',
    version='0.1.2',
    packages=find_namespace_packages(include=['zyjared.*']),
    install_requires=[],
    author='Jared Zhang',
    author_email='zyjared@outlook.com',
    description='A simple package to convert strings to colored strings using ANSI escape codes',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/zyjared/kit-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)