from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext as _build_ext
import os

# Get the current version from version.py
CURRENT_VERSION = "0.1.11"  # Adjust this accordingly

# Check if Cython is available and .pyx files are present
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'
extensions = [
    Extension("crypto_mng", [f"source_code/crypto_mng{ext}"]),
]

if USE_CYTHON:
    extensions = cythonize(extensions)

class BuildExt(_build_ext):
    def run(self):
        try:
            import numpy
            self.include_dirs.append(numpy.get_include())
        except ImportError:
            pass
        _build_ext.run(self)

setup(
    name="marearts-anpr-d",
    version="0.1.13",
    packages=find_packages(),
    ext_modules=extensions,
    cmdclass={'build_ext': BuildExt},
    package_data={'': ['*.so', '*.pyd']},
    include_package_data=True,
)
