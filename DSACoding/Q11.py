#Program for Armstrong Numbers
"""
Given a number x, determine whether the given number is Armstrong’s number or not.

A positive integer of n digits is called an Armstrong number of order n (order is the number of digits) if

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
Example: 

Input:153
Output: Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153
"""

import math
n = 153
n1 = str(n)
order = len(n1)
cum_sum=0
for i in n1:
    cum_sum += math.pow(int(i),order)
if int(cum_sum) == n:
    print("yes it is amstrong number!", cum_sum , n)


