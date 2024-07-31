from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
import sys

class BuildExt(_build_ext):
    def build_extensions(self):
        if sys.platform == "win32":
            for ext in self.extensions:
                ext.extra_compile_args = ["/std:c++11"]
        else:
            for ext in self.extensions:
                ext.extra_compile_args = ["-std=c++11"]
        super().build_extensions()

module = Extension(
    'packagePepe.pepe_cpp',
    sources=['packagePepe/pepe.cpp'],
    language='c++'
)

setup(
    name='packagePepe',
    version='0.1.0',
    description='Un paquete de ejemplo que incluye funciones en Python y C++.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://example.com/packagePepe',
    author='Tu Nombre',
    author_email='tuemail@example.com',
    packages=['packagePepe'],
    ext_modules=[module],
    cmdclass={'build_ext': BuildExt},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
