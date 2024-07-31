from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig
import setuptools.command.build_py

class build_ext(build_ext_orig):
    def run(self):
        self.run_command('build_clib')
        super().run()

cpp_module = Extension(
    'packagePepe.cpp_functions',
    sources=['packagePepe/cpp_functions.cpp'],
    extra_compile_args=['-std=c++11'],
)

setup(
    name='packagePepe',
    version='0.1.1',
    author='Tu Nombre',
    author_email='tu_email@example.com',
    description='Ejemplo de paquete con funciones en C++ y Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/tu_usuario/packagePepe',
    packages=['packagePepe'],
    ext_modules=[cpp_module],
    cmdclass={
        'build_ext': build_ext,
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
    ],
    python_requires='>=3.6',
)
