#What are Prime Numbers?
"""
A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself. 
"""
n = int(input("read number"))
if not (n%2 == 0 or n%3 == 0):
    print("yes it is prime")
else:
    print("no its not prime")