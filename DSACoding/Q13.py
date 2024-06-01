#Program to check if an array is sorted or not (Iterative and Recursive)

"""
Given an array of size n, write a program to check if it is sorted 
in ascending order or not. Equal values are allowed in an array and two consecutive equal values are considered sorted.

Examples: 

Input : 20 21 45 89 89 90
Output : Yes

Input : 20 20 45 89 89 90
Output : Yes

Input : 20 20 78 98 99 97
Output : No
"""
n = [20 ,21, 45 ,100, 89 ,90]
big=0
sort_flag=True
for i in n:
    if big <= i:
        big = i
    else:
        sort_flag=False
        print("The give number {0} is not sorted".format(n))
        break




