#define MASK 0x8000000000000000
#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>
#include "numpy/ndarraytypes.h"
//#include "numpy/ufuncobject.h"

typedef union {
    double x;
    uint64_t i;
} unf_t;


void zero_crossings_findZeroCrossings(PyArrayObject *in, PyArrayObject *out) {
    size_t i, total = 0;
    unf_t a;
    unf_t b;
    const npy_intp *shape = PyArray_SHAPE(in);
    double *y = PyArray_DATA(in);
    uint64_t *ret = PyArray_DATA(out);

    for (i = 1; i < shape[0]; ++i) {
        a.x = y[i - 1];
        b.x = y[i];
        if ((a.i & MASK) != (b.i & MASK)) {
            ret[total++] = i;
        }
    }
}

// DEF MASK = 0x8000000000000000
// ctypedef union unf_t:
//     double x
//     unsigned long i;
// @cython.profile(False)
// cpdef int findZeroCrossings(np.ndarray[np.float64_t, ndim=1] y,
//                             np.ndarray[np.uint64_t, ndim=1] ret):
//     total = 0
//     a: unf_t
//     b: unf_t
//     for i in range(1, len(y)):
//         a.x = y[i - 1]
//         b.x = y[i]
//         if a.i & MASK != b.i & MASK:
//             ret[total] = i
//             total += 1
//     return total
