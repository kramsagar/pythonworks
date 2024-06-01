##Sum of square-sums of first n natural numbers
"""
Given an integer n, find the absolute difference between sum of the squares of first n
 natural numbers and square of sum of first n natural numbers.

 
 Input : n = 3
Output : 22
Sum of first three numbers is 3 + 2 + 1 = 6
Square of the sum =  36
Sum of squares of first three is 9 + 4 + 1 = 14
Absolute difference = 36 - 14 = 22

Input : n = 10
Output : 2640

"""
n = int(input("enter input natual number range"))
sum=0
sumsq=0
for i in range(1,n+1):
    print(i)
    sum += i
    sumsq += i * i

print(sum * sum , sumsq,sum * sum - sumsq)
    


