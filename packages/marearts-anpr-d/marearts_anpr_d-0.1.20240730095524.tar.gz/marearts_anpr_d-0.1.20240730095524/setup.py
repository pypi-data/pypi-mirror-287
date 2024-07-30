from setuptools import setup, find_packages
from Cython.Build import cythonize

# Import version
with open('version.py', 'r') as f:
    exec(f.read())

setup(
    name="marearts-anpr-d",
    version=VERSION,  # Use the version from version.py
    packages=find_packages(),
    ext_modules = cythonize("source_code/crypto_mng.pyx"),
    package_data={'': ['*.pyx']},
    include_package_data=True,
)