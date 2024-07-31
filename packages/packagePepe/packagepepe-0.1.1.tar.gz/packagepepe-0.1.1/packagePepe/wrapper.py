import ctypes
import os

# Cargar la biblioteca compartida (compilada)
lib_path = os.path.join(os.path.dirname(__file__), 'cpp_functions.so')
cpp_lib = ctypes.CDLL(lib_path)

def hello_from_cpp():
    cpp_lib.hello_from_cpp()

def hello_from_python():
    print("Hello from Python!")
