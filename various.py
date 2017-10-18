import numpy as np


"""
arange and nditer
"""
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


"""
lambda and random.choice
"""
np.set_printoptions(precision=5, suppress=True)
size=10
a = np.arange(1, size+1).reshape(size, 1)
softmax = lambda x: np.exp(x) / np.sum(np.exp(x))
pick = lambda x, y: np.random.choice(range(y), p=x.ravel())
smx = softmax(a)
print("aT({})".format(a.T))
print("sT({})".format(smx.T))
for i in range(10):
    print("pick({})".format(pick(smx, size)))
np.set_printoptions(precision=8, suppress=False)

"""
aT([[ 1  2  3  4  5  6  7  8  9 10]])
sT([[ 0.00008  0.00021  0.00058  0.00157  0.00426  0.01158  0.03147  0.08555
   0.23255  0.63215]])
   pick(9)
   pick(9)
   pick(8)
   pick(8)
   pick(8)
   pick(7)
   pick(9)
   pick(6)
   pick(8)
   pick(9)
"""
