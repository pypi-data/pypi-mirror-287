from setuptools import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import os
import shutil

class CustomBuildExt(build_ext):
    def run(self):
        # Build extensions
        build_ext.run(self)
        
        # After building, remove .pyx files from the build directory
        build_lib = os.path.abspath(self.build_lib)
        for root, dirs, files in os.walk(build_lib):
            for file in files:
                if file.endswith('.pyx'):
                    os.remove(os.path.join(root, file))

# Define the extension
ext_modules = [
    Extension("marearts_anpr_d", ["license.pyx"])
]

setup(
    name="marearts-anpr-d",
    version="0.0.17",  # Increment this
    author="MareArts",
    author_email="hello@marearts.com",
    description="marearts anpr detector",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/MareArts-ANPR",
    ext_modules=cythonize(ext_modules),
    cmdclass={'build_ext': CustomBuildExt},
    py_modules=["main"],
    package_data={'': ['*.so', '*.pyd']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "marearts-anpr-d=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    license="MIT",
)