import numpy as np
from numpy.core.fromnumeric import size

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Array with random numbers of uniform distribution (only positive numbers)
random_array_uniform_distribution = np.random.rand(2, 2)
print(f'\nRandom array (uniform distribution):\n{random_array_uniform_distribution}')

# Array with random numbers of normal distribution (negative numbers included)
random_array_normal_distribution = np.random.randn(2, 2)
print(f'\nRandom array (normal distribution):\n{random_array_normal_distribution}')

# Creating a random array with a limit
random_array_with_limit = np.random.uniform(low=0, high=6, size=(4, 2)) # 'Size=(array_amount, numbers_for_array)' from 'low' to 'high'
print(f'\nRandom array with limit:\n{random_array_with_limit}')

# Similar to 'np.random.randn()' but supports scaling the sample
scaling_random_array = np.random.normal(loc=0, scale=2, size=6)
print(f'\nRandom array with escalation:\n{scaling_random_array}')

# Array with integer numbers in a range
int_random_array = np.random.randint(low=0, high=9, size=(3, 3))
print(f'\nRandom array with integers:\n{int_random_array}')
