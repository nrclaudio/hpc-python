import numpy as np

print("########## Exercise 1 ##########", end = "\n")

my_list = [1,2.5,3,5.5,7]
print("This is my list: {}".format(my_list))
my_array = np.array(my_list, dtype = 'float')
print("This is my array: {}".format(repr(my_array)))

print("########## Exercise 2 ##########", end = "\n")

second_array_arange = np.arange(-2.0, 2.2, 0.2)

print("This is my arange array: {}"
        .format(repr(second_array_arange)))

print("########## Exercise 3 ##########", end = "\n")

third_array = np.linspace(0.5, 1.5, 11)

print("This is my linspace array: {}"
	.format(repr(third_array)))

print("########## Exercise 4 ##########", end = "\n")

my_dna = "ACTGGTCA"
 
fourth_array = np.array(list(my_dna), dtype = 'S1')

print("This is my character array: {}"   
        .format(repr(fourth_array)))
