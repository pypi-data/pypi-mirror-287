#include <Python.h>

static PyObject* greet_cpp(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from C++!");
}

static PyMethodDef PepeMethods[] = {
    {"greet_cpp", greet_cpp, METH_VARARGS, "Greet from C++."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef pepemodule = {
    PyModuleDef_HEAD_INIT,
    "pepe_cpp",
    NULL,
    -1,
    PepeMethods
};

PyMODINIT_FUNC PyInit_pepe_cpp(void) {
    return PyModule_Create(&pepemodule);
}
