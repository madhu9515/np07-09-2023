import numpy as np
arr=np.arange(6)
arr1=np.linspace(0,10) #by default 3arg is 50 it gives no. of arguments in b/t 2 arguments
print(arr1)
arr2=np.linspace(0,10,5)
print(arr2)
arr3=np.linspace(0,10,5,endpoint=False)
print(arr3)
arr4=np.linspace(0,10,5,endpoint=False,retstep=True)
print(arr4)
arr5=np.linspace(0,10,5,endpoint=False,retstep=True,dtype=int)
print(arr5)
