import numpy as np

first_array = np.zeros((4,4), float)

first_array[1,:]
first_array[:,2]
first_array[:2,:2] = 0.21
print(first_array)


second_array  = np.zeros((8,8), float)

second_array[::2, ::2] = 1
second_array[1::2, 1::2] = 1
print(second_array)

