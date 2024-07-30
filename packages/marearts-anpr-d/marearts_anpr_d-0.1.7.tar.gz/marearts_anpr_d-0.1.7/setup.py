from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="marearts-anpr-d",
    version="0.1.7",
    packages=find_packages(),
    ext_modules = cythonize("source_code/crypto_mng.pyx"),
    package_data={'': ['*.pyx']},
    include_package_data=True,
)
