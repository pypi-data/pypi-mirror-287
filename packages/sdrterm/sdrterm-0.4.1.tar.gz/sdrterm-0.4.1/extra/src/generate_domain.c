#define PY_SSIZE_T_CLEAN
#include <Python.h>

PyObject *generateDomain(const char c) {
    switch (c) {
         case 'B':
             return Py_BuildValue("(BB)", 0, 255);
         case 'b':
             return Py_BuildValue("(bb)", -128, 127);
         case 'H':
             return Py_BuildValue("(HH)", 0, 65536);
         case 'h':
             return Py_BuildValue("(hh)", -32768, 32767);
         case 'I':
             return Py_BuildValue("(kk)", 0UL, 4294967295UL);
         case 'i':
             return Py_BuildValue("(ll)", -2147483648L, 2147483647L);
         case 'L':
             return Py_BuildValue("(KK)", 0ULL, 18446744073709551615ULL);
         case 'l':
             return Py_BuildValue("(nL)", 0x8000000000000000, 9223372036854775807LL);
         default:
            return NULL;
    }
}
