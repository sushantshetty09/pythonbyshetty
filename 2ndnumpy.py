# # # import numpy as np
# # # arr=np.array([1,2,3,4,5])
# # # print(arr)
# # # numbers=np.array([1,2,3,4,5,6,])
# # # print(numbers)
# # # print(numbers.ndim)
# # # print(numbers.shape)

# # import numpy as np
# # arr=np.array([[1,2,3],[1,2,3],[3,4,5]])
# # print(arr)
# # print(arr.ndim)
# # print(arr.shape)
# # print(arr.size)
# # print(arr.dtype)
# # print(arr.itemsize)

# ######## creating numpy array from functions ########
# import numpy as np
# arr=np.arange(1,10,2)
# print(arr)
# b=np.arange(100,0,-10)
# print(b)


# a=np.linspace(1,10,5) # start, stop, number of elements
# print(a)

import numpy as np
a=np.zeros((2,8))
print(a)
b=np.ones((9,9))
print(b)
c=np.eye((3))
print(c)
print(type(c))