"""
Types:
Integer
    octal (0o123 = 8^2*1 + 8^1 *2 + 8^0 *3)
    hexa  (0x123 = 16^2*1 + 16^1 *2 + 16^0 *3)
Floating
string
boolean

base = 2
exponent = 3
print(base**exponent) 

"""

print(0o11)
print(0x11)
base = 6
exponent = 2
print(base**exponent) 
print(base%exponent) 
print(base/exponent)
base = 25
exponent = -5
print(base**exponent)
r = pow(2, 3)
print(r) # 8

print(pow(3, 4))
r = pow(3, 4, 5) #This is equal to = 3^4%5
print(r)  # 1

import numpy as np
r = np.power([2, 4, 8], 2)
print(r)  # [4, 16, 64]

import math
x = 1
r = math.exp(x) #e^1
print("Exponential of", x, ":", r) # 2.718281828459045

print(int(True))

"""
(.venv) PS D:\mydrive\DevopsWorks\PythonWork> python .\Literals.py   
9
17
36
0
3.0
1.024e-07
8
81
1
[ 4 16 64]
Exponential of 1 : 2.718281828459045
"""


