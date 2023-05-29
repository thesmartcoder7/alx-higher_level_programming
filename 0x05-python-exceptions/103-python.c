#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_float - gives the PyFloatObject data
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double sm_val = 0;
	char *sm_str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	sm_val = ((PyFloatObject *)p)->ob_fval;
	sm_str = PyOS_double_to_string(sm_val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", sm_str);
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *sm_item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			sm_item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, sm_item->ob_type->tp_name);
			if (PyBytes_Check(sm_item))
				print_python_bytes(sm_item);
			else if (PyFloat_Check(sm_item))
				print_python_float(sm_item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
