#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    PyObject *list_size = PyObject_Length(p);
    PyObject *allocated = PyObject_GetAttrString(p, "allocated");
    Py_ssize_t size = PyLong_AsSsize_t(list_size);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", PyLong_AsSsize_t(allocated));

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        PyObject *item_type = PyObject_GetAttrString(item, "__class__");
        PyObject *type_name = PyObject_GetAttrString(item_type, "__name__");

        printf("Element %zd: %s\n", i, PyUnicode_AsUTF8(type_name));

        if (strcmp(PyUnicode_AsUTF8(type_name), "bytes") == 0)
            print_python_bytes(item);

        Py_DECREF(item_type);
        Py_DECREF(type_name);
    }

    Py_DECREF(list_size);
    Py_DECREF(allocated);
}

void print_python_bytes(PyObject *p) {
    PyObject *size_obj = PyObject_Length(p);
    Py_ssize_t size = PyLong_AsSsize_t(size_obj);
    Py_ssize_t i;
    char *bytes_repr;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        Py_DECREF(size_obj);
        return;
    }

    printf("  size: %zd\n", size);

    if (size > 10)
        size = 10;

    bytes_repr = PyBytes_AsString(p);

    printf("  trying string: %s\n", bytes_repr);

    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02hhx", bytes_repr[i]);
        if (i == size - 1)
            printf("\n");
        else
            printf(" ");
    }

    Py_DECREF(size_obj);
}