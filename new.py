import numpy as np

number =np.array([1,2,3,4,5,6,7,8,9,10])

even_number = number[number %2 ==0]
print(even_number)

