import ctypes
import os
import pkg_resources
dist = pkg_resources.get_distribution('packagePepe')

# Determinar la extensión de la biblioteca compartida según el sistema operativo
if os.name == "nt":
    lib_name = "cpp_functions.cp312-win_amd64.pyd"
else:
    lib_name = "cpp_functions.so"

# Ruta a la biblioteca compartida compilada
lib_path = os.path.join(os.path.dirname(__file__), lib_name)
cpp_lib = ctypes.CDLL(lib_path)

def hello_from_cpp():
    cpp_lib.hello_from_cpp()

def hello_from_python():
    print("Hello from Python!")
