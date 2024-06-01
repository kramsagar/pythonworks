#Program to count vowels in a string
"""
Given a string, count the total number of vowels (a, e, i, o, u) in it. 
There are two methods to count total number of vowels in a string. 

Iterative 
Recursive

Input : abc de
Output : 2

Input : geeksforgeeks portal
Output : 7
"""

str = "geeksforgeeks portal"
a=['a','e','i','o']
i=0
while i < len(str):
    if a.__contains__(str[i]):
        print("yes its vowel", str[i], i+1)

    i += 1

