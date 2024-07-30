from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Get the absolute path of the directory containing this script (setup.py)
here = os.path.abspath(os.path.dirname(__file__))

# Construct the full path to license.pyx
license_pyx_path = os.path.join(here, 'license.pyx')

# Ensure the file exists
if not os.path.exists(license_pyx_path):
    raise FileNotFoundError(f"Cannot find the file 'license.pyx' at {license_pyx_path}")

# Define the extension
extensions = [Extension("marearts_anpr_d", [license_pyx_path])]

setup(
    name="marearts-anpr-d",
    version="0.0.8",
    author="MareArts",
    author_email="hello@marearts.com",
    description="marearts anpr detector",
    long_description=open(os.path.join(here, 'README.md'), 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/MareArts-ANPR",
    ext_modules=cythonize(extensions),
    py_modules=["main"],
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