# setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("Netaxgene.network", ["Netaxgene/network.pyx"]),
]

setup(
    name="Netaxgene",
    version="0.1.1",
    description="A package for generating network files",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Gongruihao",
    author_email="202031200039@mail.bnu.edu.cn",
    packages=["Netaxgene"],
    ext_modules=cythonize(extensions),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
