#Program for Sum of the digits of a given number
"""
Input: n = 687
Output: 21

Input: n = 12
Output: 3
"""
n = 12
n1 = str(n)
i = 0
sum=0
while i < len(n1):
    sum += int(n1[i])
    i += 1

print(sum) 