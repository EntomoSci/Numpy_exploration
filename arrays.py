import numpy as np


# Creating vectors (unidimensional arrays)
vector_a = np.arange(5) # 0 to 4 array
vector_b = np.arange(3, 7, 1) # start, stop, step

print(f'\nVector A:\n', vector_a)
print(f'\nVector B:\n', vector_b)


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

