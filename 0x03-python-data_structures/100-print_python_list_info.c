#include <Python.h>

void print_python_list_info(PyObject *p)
{
	PyObject *data;
	Py_ssize_t size, allocated, idx;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (idx = 0; idx < size; idx++)
	{
		data = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, data->ob_type->tp_name);
	}
}
