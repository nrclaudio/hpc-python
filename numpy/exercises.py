import numpy as np
import matplotlib.pyplot as plt


# ALWAYS REMEMBER PYTHON SLICING [START:END); THE START IS INCLUDED, THE END IS NOT


# EXERCISE 1: ARRAY CREATION

print("########## 1.1 ##########\n")

my_list = [1, 2.5, 3, 5.5, 7]
print("This is my list: {}".format(my_list))
my_array = np.array(my_list, dtype="float")
print("This is my array: {}".format(repr(my_array)))

print("\n########## 1.2 ##########\n")

second_array_arange = np.arange(-2.0, 2.2, 0.2)
print("This is my arange array: {}"
      .format(repr(second_array_arange)))

print("\n########## 1.3 ##########\n")

third_array = np.linspace(0.5, 1.5, 11)
print("This is my linspace array: {}"
      .format(repr(third_array)))

print("\n########## 1.4 ##########\n")

my_dna = "ACTGGTCA"

fourth_array = np.array(list(my_dna), dtype='S1')

print("This is my character array: {}\n"
      .format(repr(fourth_array)))


# EXERCISE 2: ARRAY CREATION

first_array = np.random.rand(4, 4)
print(first_array)

print("\n########## 2.1 ##########\n")
print(first_array[1, :])

print("\n########## 2.2 ##########\n")
print(first_array[:, 2])

print("\n########## 2.3 ##########\n")
first_array[:1, :1] = 0.21
print(first_array)

print("\n########## 2.4 ##########\n")
second_array = np.zeros((8, 8), float)

second_array[::2, ::2] = 1
second_array[1::2, 1::2] = 1
print(second_array)

# EXERCISE 3: VECTORIZATION

print("\n########## 3 ##########\n")

step = 0.1
start = 0
end = np.pi / 2

x = np.arange(start, end, step)
sol_sin = (np.sin(x[2:]) - np.sin(x[:-2])) / (2 * step)
print(sol_sin)

sol_cos = np.cos(x[1:-1])
print("Mean squared difference: \n")
print(np.sqrt(np.sum((sol_sin - sol_cos)**2)))

# EXERCISE 4: VECTORIZATION 2

print("\n########## 4 ##########\n")

start = 0
end = np.pi / 2
dx = 0.1

x = np.arange(start, np.pi / 2, dx)
x_riem = np.sum(np.sin(x) * dx)

print("Riemann sum: {0:f}".format(x_riem))

# EXERCISE 5: SPLIT AND COMBINE

print("\n########## 5 ##########\n")

a = np.random.rand(8, 8)
print(a.shape)

b, c = np.split(a, 2)
print(b.shape, c.shape)
e, f = np.split(a, 2, axis=1)
print(e.shape, f.shape)

d = np.concatenate((b, c))
print(d.shape)
g = np.concatenate((e, f))
print(g.shape)


# EXERCISE 6: TRANSLATION WITH BROADCASTING

print("\n########## 6 ##########\n")


arr = np.genfromtxt('/Users/claudionovellarausell/hpc-python/numpy/broadcast-translation/points_circle.dat')
trans = np.array([2.1, 1.1])
new_arr = arr * trans

plt.plot(arr[:, 0], arr[:, 1], 'o')
plt.plot(new_arr[:, 0], new_arr[:, 1], 'o')
plt.show()


# EXERCISE 7: FILE I/O

print("\n########## 7 ##########\n")

arr = np.loadtxt('/Users/claudionovellarausell/hpc-python/numpy/input-output/xy-coordinates.dat')

arr[:, 1] += 2.5

np.savetxt('/Users/claudionovellarausell/hpc-python/numpy/input-output/new_xy-coordinates.dat', new_arr)

# EXERCISE 8: RANDOM NUMBERS
