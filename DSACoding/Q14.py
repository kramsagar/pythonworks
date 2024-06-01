#Program to print multiplication table of a number
"""
Given a number n as input, we need to print its table. 
Input :  5
Output : 5 * 1 = 5
         5 * 2 = 10
         5 * 3 = 15
         5 * 4 = 20
         5 * 5 = 25
         5 * 6 = 30
         5 * 7 = 35
         5 * 8 = 40
         5 * 9 = 45
         5 * 10 = 50
"""
n = int(input("read number"))
for i in range(1,11):
    print(" {0} X {1} = {2}".format(n,i, n *i))
