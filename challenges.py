import numpy as np

# Create a 3D tensor from lists
tensor_from_lists = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]],
])
print(f'\n3D tensor from list:\n{tensor_from_lists}')

# Create an array with 100 values between 6 and 9
array = np.linspace(start=6, stop=9, num=100)
print(f'\nArray with 100 values between 6 and 9:\n{array}')

# Reuse the previous array base with pi values
reused_array = np.full_like(a=array, fill_value=np.pi)
print(f'\nReusing previous array base with pi values:\n{reused_array}')

# Create 1D array with 10,000 random numbers
vector_with_10000_random_numbers = np.random.randn(10000)
print(f'\nVector with 10,000 random numbers:\n{vector_with_10000_random_numbers}')
