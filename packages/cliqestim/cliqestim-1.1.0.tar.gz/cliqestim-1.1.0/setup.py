# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("cliqestim.cli", ["cliqestim/cli.pyx"]),
]

setup(
    name="cliqestim",
    version="1.1.0",
    description="A package for estimating clique structure",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Gongruihao",
    author_email="202031200039@mail.bnu.edu.cn",
    
    packages=["cliqestim"],
    ext_modules=cythonize(extensions),
    install_requires=[
        'cdlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
