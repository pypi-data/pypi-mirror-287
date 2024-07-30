from setuptools import setup, Extension, Command, find_packages
from setuptools.command.sdist import sdist
from setuptools.command.bdist_wheel import bdist_wheel
from Cython.Build import cythonize
import sys
import os

class CleanCommand(Command):
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass
    def run(self):
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.c') or file.endswith('.pyx'):  # Remove .c and .pyx files
                    os.remove(os.path.join(root, file))
                    print(f"Removed: {os.path.join(root, file)}")

class CustomSdist(sdist):
    def run(self):
        self.run_command('build_ext')
        sdist.run(self)
        self.run_command('clean')  # Clean after creating sdist

class CustomBdistWheel(bdist_wheel):
    def run(self):
        self.run_command('build_ext')
        bdist_wheel.run(self)
        self.run_command('clean')  # Clean after creating wheel

# Define the extension
extensions = [Extension("marearts_myapp_compiled", ["myapp.pyx"])]

# On Windows, we need to specify additional compile args
if sys.platform == "win32":
    for e in extensions:
        e.extra_compile_args = ["/O2"]

# Handle the absence of README.md
long_description = ""
if os.path.exists('README.md'):
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()

# Read dependencies from requirements.txt
def parse_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

requirements = []
if os.path.exists('requirements.txt'):
    requirements = parse_requirements('requirements.txt')

setup(
    name="marearts-anpr-d",
    version="0.0.36",  # Increment this
    author="MareArts",
    author_email="hello@marearts.com",
    description="A short description of your application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/pypi_test",
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    install_requires=requirements,
    py_modules=["run_myapp"],
    entry_points={
        "console_scripts": [
            "marearts-anpr-d=run_myapp:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    cmdclass={
        'clean': CleanCommand,
        'sdist': CustomSdist,
        'bdist_wheel': CustomBdistWheel,
    },
    license="MIT",
    package_data={
        '': ['*.pyd', '*.so'],
    },
    exclude_package_data={
        '': ['*.pyx', '*.c'],
    },
    include_package_data=True,  # Ensure MANIFEST.in is included
)
