from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
import os

# Check if Cython is available and .pyx files are present
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

def get_extensions():
    if USE_CYTHON and os.path.exists("marearts_anpr_d/crypto_mng.pyx"):
        extensions = [Extension("crypto_mng", ["marearts_anpr_d/crypto_mng.pyx"])]
        return cythonize(extensions, language_level="3")
    else:
        extensions = [Extension("crypto_mng", ["marearts_anpr_d/crypto_mng.c"])]
        return extensions

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
    version="0.1.0",
    packages=['marearts_anpr_d'],
    ext_modules=get_extensions(),
    cmdclass={'build_ext': BuildExt},
    package_data={'': ['*.so', '*.pyd']},
    include_package_data=True,
    python_requires='>=3.10',
)