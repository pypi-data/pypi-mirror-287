from setuptools import setup, Extension
from Cython.Build import cythonize

# ... (otros imports si necesarios)

# Extensión para compilar el código C++
extension = Extension(
    "packagePepe.module_cpp",
    sources=["packagePepe/cpp_functions.cpp"],
    # ... (otras opciones de compilación, si es necesario)
)

setup(
    name="packagePepe",
    version="0.1.7",
    description="Mi primer paquete con C++ y Python",
    author="Tu Nombre",
    author_email="tu_email@example.com",
    packages=["packagePepe"],
    ext_modules=cythonize(extension),
)
