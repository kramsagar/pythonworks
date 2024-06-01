#Segregate 0s and 1s in an array
"""
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s 
on right side of the array [Basically you have to sort the array]. Traverse array only once. 

Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 
"""

list1 = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
"""
list1.sort()
print(list1)
"""
ones,zeros=0,0
lenth = len(list1)
for i in list1:
    if i == 0:
        zeros+=1
    else:
        ones+=1
new_list=[]
for i in range(0,zeros-1):
    new_list.append(0)
for i in range(0,ones-1):
    new_list.append(1)
print(new_list)
