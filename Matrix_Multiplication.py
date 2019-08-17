import numpy as np

#numpy.matmul


# 2-D matrix product

a = np.array([[1, 0], [0, 1]])
b = np.array([[4, 1], [2, 2]])
c = np.array([[4, 1], [2, 2]])

x = np.matmul(a, b)


layer_0 = np.array([[n_0,n_1], [n_2,n_3]])
layer_1 = np.array([[n_4,n_5], [n_6,n_7]])
layer_2 = np.array([[n_8,n_9], [n_10,n_11]])


#print(x)

#a = np.array([[1, 0], [0, 1])

#broadcasting conventional for stacks of arrays

c = np.arange(2 * 2 * 4).reshape((2, 2, 4))
d = np.arange(2 * 2 * 4).reshape((2, 4, 2))

x_1 = np.matmul(c, d).shape

print(x_1)

x_2 = np.matmula(c, d)[0, 1, 1]

print(x_2)

x_3 = sum(c[0, 1, :] * d[0, :, 1])

print(x_3)

#Vector returns the scalar inner product, but neither argument is complex-conjugated

x_4 = np.matmul([2j, 3j, [2j, 3j])

print(x_4)


