from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os


extensions = [
    Extension("crypto_mng", ["source_code/crypto_mng.pyx"]),
]

setup(
    name="marearts-anpr-d",
    version="0.1.12",
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    package_data={'': ['*.so', '*.pyd']},
    include_package_data=True,
)
