age=[1,3,2]

print("Initial : ",age)
print("lenth : ",len(age))
print("age[1]: ", age[1])
print("age[-1]: ",age[-1])
print("age[-2]: ",age[-2])
print("age[-3]: ",age[-3])

#deleting
del age[0]
print("after deleting index=0 ",age)

#list methods
age.append(123); print("Append 123 age:",age)  #insert only at the end.
age.insert(0,1); print("insert 1 at index=0 ",age)   #insert in middle of the list


#swap the items in the list.
age[0],age[1],age[2],age[3] = age[1],age[0],age[3],age[2]
print("After swapping all 4 items ",age)

#sort 
age.sort(); print("sort: ",age)
#reverse
age.reverse(); print("reverse: ",age)

"""
Initial :  [1, 3, 2]
lenth :  3
age[1]:  3
age[-1]:  2
age[-2]:  3
age[-3]:  1
after deleting index=0  [3, 2]
Append 123 age: [3, 2, 123]
insert 1 at index=0  [1, 3, 2, 123]
After swapping all 4 items  [3, 1, 123, 2]
sort:  [1, 2, 3, 123]
reverse:  [123, 3, 2, 1]
"""