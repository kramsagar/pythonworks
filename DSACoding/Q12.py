#Program for factorial of a number
"""
What is the factorial of a number?
Factorial of a non-negative integer is the multiplication of all positive integers smaller than or equal to n. 
For example factorial of 6 is 6*5*4*3*2*1 which is 720. 
A factorial is represented by a number and a  ” ! ”  mark at the end. It is widely used in permutations 
and combinations to calculate the total possible outcomes. A French mathematician Christian Kramp firstly used the exclamation.


"""
n = int(input("read number"))
fact=1
for i in range(1,n+1):
    fact *= i

print("Factorial of {0} is {1}".format(n,fact))
