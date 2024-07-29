# cython: profile=False
# cython: nonecheck=False
# cython: boundscheck=False
# cython: overflowcheck=False
# cython: cdivision=True
# cython: language_level=3
# cython: infer_types=False
# TODO remove and append EVERY SINGLE CDEF LINE with noexcept, when this is finally removed.
# cython: legacy_no_except=True
# cython: show_performance_hints=True

cimport cython
cimport numpy as np; np.import_array()
from numpy cimport ndarray

from numpy import conj, angle
from scipy import signal

cpdef void demodulateFm(ndarray[np.complex128_t] y, ndarray[np.float64_t] ret):
    ret[:] = signal.resample(angle(y[0::2] * conj(y[1::2])), y.size)

cpdef void normalize(ndarray x,
                ndarray[np.float64_t, ndim=1] ret,
                tuple[cython.double, cython.double] rnge,
                const double a,
                const double b):
    cdef double rcpXMaxMinDiff = 1. / (rnge[1] - rnge[0])
    ret[:] = (b - a) * (x - rnge[0]) * rcpXMaxMinDiff + a

cdef extern from "generate_domain.c":
    # cdef const (int, int) generateDomain(const char *c)
    # cpdef tuple[int64 | uint64, int64 | uint64, int64 | uint64] generateDomain(const char *c)

    cpdef tuple[cython.Shadow.py_int, cython.Shadow.py_int] generateDomain(const char c) nogil

cdef extern from "zero_crossings.c":

    cpdef void findZeroCrossings(ndarray[np.float64_t, ndim=1] y, ndarray[np.uint64_t, ndim=1] ret) nogil