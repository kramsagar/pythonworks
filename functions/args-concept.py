def show(age1):
    age1*=10
    print("print age: ",age1)

age=10
show(age)
print("show age: ",age)


def show(l):
    l.append(100)

l=[1,10]
print("before sending list to function",l)
show(l)
print("after sending list to function",l)

"""
print age:  100
show age:  10
before sending list to function [1, 10]
after sending list to function [1, 10, 100]
"""