import numpy as np
#zeros
arr=np.zeros(3,dtype=int)
print(arr)
arr1=np.zeros((2,3),dtype=float)              #by default dtype is float
print(arr1)
#ones same as zeros
arr2=np.ones((3,2,2),dtype=int)
print(arr2)
#full
arr3=np.full((2,3),5,dtype=int)            #2 arguments are mandatory
print(arr3)
#
arr4=np.eye(3,dtype=int)                  #1 argument is mandatory
print(arr4)


