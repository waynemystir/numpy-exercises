import numpy as np

a = np.arange(10, 20).reshape(2, 5)
# a = np.linspace(10, 19, 10, dtype=int).reshape(2, 5)
it = np.nditer(a, flags=['multi_index'])

while not it.finished:
    print("it0(%d) mi0(%d) mi1(%d) mi(%s)" % (it[0], it.multi_index[0], it.multi_index[1], it.multi_index))
    it.iternext()

"""
it0(10) mi0(0) mi1(0) mi((0, 0))
it0(11) mi0(0) mi1(1) mi((0, 1))
it0(12) mi0(0) mi1(2) mi((0, 2))
it0(13) mi0(0) mi1(3) mi((0, 3))
it0(14) mi0(0) mi1(4) mi((0, 4))
it0(15) mi0(1) mi1(0) mi((1, 0))
it0(16) mi0(1) mi1(1) mi((1, 1))
it0(17) mi0(1) mi1(2) mi((1, 2))
it0(18) mi0(1) mi1(3) mi((1, 3))
it0(19) mi0(1) mi1(4) mi((1, 4))
"""
