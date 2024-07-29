import os
import subprocess
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        super().__init__(name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = [
            f'-DPYTHON_EXECUTABLE={sys.executable}',
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
        ]

        build_args = []

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

setup(
    name='mstmap',
    version='1.0.1',
    author='Amirsadra Mohseni',
    author_email='amohs002@ucr.edu',
    description='A C++ library for genetic mapping with pybind11 interface',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    ext_modules=[CMakeExtension('mstmap')],
    cmdclass={
        'build_ext': CMakeBuild,
    },
    zip_safe=False,
    python_requires='>=3.7',
)
