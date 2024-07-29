from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("quickquant.module", ["quickquant/module.pyx"]),
]

setup(
    name="quickquant",
    version="0.1",
    author="Nabarup Ghosh",
    author_email="nabarupeducation@gmail.com",
    description="A fast quant finance library using Cython",
    ext_modules=cythonize(extensions),
    license="Apache License 2.0",
    packages=["quickquant"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
