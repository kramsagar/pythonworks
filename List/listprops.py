age=[10,12,12,13]
print("Initial age ",age)

#copy by reference
age1 = age 
age1[0] = 11
print("age1 ",age1)
print("age ",age)

#slicing
age2 = age[0:len(age)]
print("Initial age2 ", age2)
age2[0] = 111
print("Age2 ",age2)
print("Age ",age)

"""
Initial age  [10, 12, 12, 13]
age1  [11, 12, 12, 13]
age  [11, 12, 12, 13]
Initial age2  [11, 12, 12, 13]
Age2  [111, 12, 12, 13]
Age  [11, 12, 12, 13]
"""