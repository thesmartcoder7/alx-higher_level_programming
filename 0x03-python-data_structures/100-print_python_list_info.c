#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
    PyListObject *list;
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Invalid List Object\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}