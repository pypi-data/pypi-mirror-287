from setuptools import setup, Extension, Command
from setuptools.command.sdist import sdist as _sdist
from setuptools.command.bdist_wheel import bdist_wheel
from Cython.Build import cythonize
import sys
import os

class sdist(_sdist):
    def run(self):
        # Make sure the compiled Cython files are included in the source
        # distribution
        cythonize(["myapp.pyx"])
        _sdist.run(self)

class RemovePyxCommand(Command):
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        # Remove .pyx files after build
        for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            for file in files:
                if file.endswith('.pyx'):
                    try:
                        os.remove(os.path.join(root, file))
                        print(f"Removed: {file}")
                    except OSError as e:
                        print(f"Error removing {file}: {e}")

class CustomSdist(sdist):
    def run(self):
        self.run_command('build_ext')
        self.run_command('remove_pyx')
        sdist.run(self)

class CustomBdistWheel(bdist_wheel):
    def run(self):
        self.run_command('build_ext')
        self.run_command('remove_pyx')
        bdist_wheel.run(self)

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
    version="0.0.20",  # Increment the version
    author="MareArts",
    author_email="hello@marearts.com",
    description="A short description of your application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MareArts/pypi_test",
    ext_modules=cythonize(extensions),
    install_requires=requirements,
    py_modules=["run_myapp"],
    entry_points={
        "console_scripts": [
            "marearts-anpr-d=run_myapp:main",
        ],
    },
    # cmdclass={
    #     'remove_pyx': RemovePyxCommand,
    #     'sdist': CustomSdist,
    #     'bdist_wheel': CustomBdistWheel,
    # },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    cmdclass={
        'sdist': sdist,
    },
    license="MIT",
)