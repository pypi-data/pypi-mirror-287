# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("Netaxgenespo.network", ["Netaxgenespo/network.pyx"]),
]

setup(
    name="Netaxgenespo",
    version="0.1.1",
    description="A package for generating network files",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=["Netaxgenespo"],
    ext_modules=cythonize(extensions),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
