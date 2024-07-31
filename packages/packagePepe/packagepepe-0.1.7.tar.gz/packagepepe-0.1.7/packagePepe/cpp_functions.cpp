#include <Python.h>

static PyObject* wrapper_funcion_cpp(PyObject *self, PyObject *args) {
    // ... lógica en C++
    return Py_BuildValue("s", "Hola desde C++!");
}

static PyMethodDef Methods[] = {
    {"funcion_cpp", wrapper_funcion_cpp, METH_VARARGS, "Documentación de la función"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "packagePepe.module_cpp",
    "Módulo C++ para packagePepe",
    -1,
    Methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyMODINIT_FUNC PyInit_module_cpp(void) {
    return PyModule_Create(&moduledef);
}
