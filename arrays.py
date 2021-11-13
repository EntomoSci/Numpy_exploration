import numpy as np


# Creating vectors (unidimensional arrays)
vector_a = np.arange(5) # 0 to 4 array
vector_b = np.arange(3, 7, 1) # start, stop, step
vector_c = np.arange(11, 1, -2)
vector_d = np.linspace(0, 1, num=11) # Automatic step calculation with explicit array length definition (third parameter)

print(f'\nVector A:\n', vector_a)
print(f'\nVector B:\n', vector_b)
print(f'\nVector C:\n', vector_c)
print(f'\nVector D:\n', vector_d)


# Creating matrix (bidimensional arrays)
matrix_a = np.arange(9).reshape(3, 3) # Array of 3 arrays each one with 3 ascendent numbers from 0 to reach 8

# for index, array in enumerate(matrix_a):
#     print(f'{index} array:', array)
#     for element in array:
#         print(element)
print(f'\nMatrix:\n', matrix_a)


# Creating tensors (+3 dimensional arrays)
tensor_a = np.arange(12).reshape(3, 2, 2)

print(f'\nTensor:\n', tensor_a)


# Creating an array from a list
my_list = [1, 2, 3, 4, 5]

vector_from_list_a = np.array(my_list)
vector_from_list_b = np.array([1, 2, 3, 4, 5])
print(f'\nVector from list A:\n', vector_from_list_a)
print(f'\nVector from list B:\n', vector_from_list_b)

matrix_from_list = np.array([[1, 2, 3], [4, 5, 6]])
print(f'\nMatrix from list:\n', matrix_from_list)

tensor_from_list = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(f'\nTensor from list:\n', tensor_from_list)


# Creating empty arrays
empty_array_a = np.zeros(5)
empty_array_b = np.zeros((2, 2))
empty_array_c = np.ones((2, 2))

print(f'\nEmpty array A:\n{empty_array_a}')
print(f'\nEmpty array B:\n{empty_array_b}')
print(f'\nEmpty array C:\n{empty_array_c}')


# Filled arrays
filled_array_a = np.full(shape=(2, 2), fill_value=7)
filled_array_b = np.full(shape=(2, 2), fill_value='a')

print(f'\nFilled array A:\n{filled_array_a}')
print(f'\nFilled array B:\n{filled_array_b}')


# Reusing the structure of an array to construct another array
base = np.linspace(2, 6, 4)
reuse_array_a = np.full_like(base, np.pi)

print(f'\nReuse array A:\nBase: {base}\nTo: {reuse_array_a}\n')
