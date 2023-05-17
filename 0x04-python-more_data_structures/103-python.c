#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type);
    }
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size;
    Py_ssize_t i;
    char *bytes;
    char *byte_repr;

    printf("[.] Bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);

    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", bytes);

    if (size > 10)
        size = 10;

    byte_repr = malloc((size * 4) + 1);
    if (byte_repr == NULL)
    {
        printf("  [ERROR] Failed to allocate memory\n");
        return;
    }

    for (i = 0; i < size; i++)
    {
        sprintf(byte_repr + (i * 4), "%.2hhx ", bytes[i]);
    }
    byte_repr[size * 4] = '\0';

    printf("  First %ld bytes: %s\n", size, byte_repr);

    free(byte_repr);
}
