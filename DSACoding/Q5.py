#Check if a number is Palindrome
"""
Given a positive integer, write a function that returns true if the given number is a 
palindrome, else false. For example, 12321 is a palindrome, but 1451 is not a palindrome. 
"""

n=122221
n1 = str(n)
n2=""
i = len(n1)-1
while i < len(n1) and i >=0:
    print(n1[i])
    n2 = n2 + n1[i]
    i -= 1

print(int(n2) == n)

"""
i=0
iter=0
if len(n)%2 == 0:
    iter=len(n)/2
else:
    iter=int(len(n)/2) +1
j=-1
palen=0
while i < iter:
    if n[i] == n[j]:
        palen+=1
    i+=1
    j-=1

if palen == iter:
    print("yes number is palen",n)
else:
    print("No its not! ",n)
"""