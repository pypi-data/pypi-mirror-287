import math

import numpy as np

from dsp.iq_correction import IQCorrection
from dsp.fast import iq_correction
# import main

EPSILON = 10E-9
DEBUG = False


# def test_1():
#     foo = np.array([-1, -2, 3, -4, 5], dtype=np.float64)
#     bar = np.zeros(foo.size >> 1 if not foo.size & 1 else (foo.size >> 1) + 1, dtype=np.uint64)
#     main.findZeroCrossings(foo, bar)
#     for m, n in zip(bar, [2, 3, 4]):
#         assert m == n
#         # assert np.sign(foo[n - 1]) != np.sign(foo[n])
#         assert math.copysign(foo[n - 1], foo[n]) != foo[n - 1]


# def test_3():
#     boo = [0.1798535, 0.10197261, 0.02409172, 0.10197261]
#     foo = np.array([1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])
#     bar = np.zeros(foo.size)
#     main.demodulateFm(foo, bar)
#     for i, (x, y) in enumerate(zip(bar, boo)):
#         assert np.fabs(x - y) < EPSILON


def test_4():
    fs = 1000
    iqc = IQCorrection(fs)
    iqc1 = iq_correction.IQCorrection(fs)
    data = np.array([1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])
    tmp = np.array([1 + 2j, 3 + 4j, 5 + 6j, 7 + 8j])

    iqc.correctIq(data)
    iqc1.correctIq(tmp)
    for x, y in zip(data, tmp):
        assert np.fabs(x.real - y.real) < EPSILON
        assert np.fabs(x.imag - y.imag) < EPSILON


# def evalError(chars: np.ndarray[any, np.uint8]):
#     res = 0
#     tss = 0
#     total = 0
#     cavg = 0
#     avgs = []
#     ests = []
#     ts = 1 / (1 << 20)
#     expv = np.arange(-0.8, 0.8, 1.6 * ts)  # (-a+b)/step = 2*0.8/256
#     for c in chars:
#         dmin, dmax = domain = main.generateDomain(c)
#         data = np.array(np.arange(dmin, dmax, (-dmin + dmax) * ts))
#         est = np.zeros(data.size)
#         main.normalize(data, est, domain, -0.8, 0.8)
#         diff = expv - est
#         assert (np.fabs(diff) < EPSILON).all()
#
#         res += np.sum(np.square(diff))
#         total += est.size
#         cavg += np.sum(est - cavg) / total
#         tss += np.sum(np.square(est - cavg))
#         if DEBUG:
#             ests.extend(est)
#             avgs.append(np.mean(est))
#     rsq = 1 - res / tss
#     if DEBUG:
#         ests = np.array(ests)
#         avg = np.mean(ests)
#         avgs = np.mean(avgs)
#         print(f'\n{avg} {avgs} {cavg}')
#         print(
#             f'{1 - res / np.sum(np.square((ests - avg)))} {1 - res / np.sum(np.square((ests - avgs)))} {rsq}')
#     return rsq
#
#
# def test_5():
#     # vals = (0, 255, -128, 127, 0, 65536, -32768, 32767, 0, 4294967295, -2147483648, 2147483647,
#     #         0, 18446744073709551615, -9223372036854775808, 9223372036854775807)
#     tmp = (b'B', b'b', b'H', b'h', b'I', b'i', b'L', b'l')
#     rsq = evalError(np.array([int(x.hex(), 16) for x in tmp], dtype=np.uint8))
#     print(f'\n{rsq}')
#     assert rsq > 0.999
