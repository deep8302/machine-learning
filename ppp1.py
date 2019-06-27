#!/usr/bin/python3

import numpy as np


a=int(input("how many number of rows you want: "))
b=int(input("how many number of column you want: "))

c = np.random.random((a,b))
print(c)

np.savetxt("array.txt", np.array(c), fmt="%s")





