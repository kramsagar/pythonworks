#Check if given number is perfect square
"""
Input : n = 2500
Output : Yes
Explanation: 2500 is a perfect square of 50

Input : n = 2555
Output : No
"""
import math as m
n=625
m =m.sqrt(n)
if  m * m == n:
    print("yes it is perfect sqrt!")
else:
    print("No its not")
