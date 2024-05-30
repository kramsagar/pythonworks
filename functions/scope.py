### within functions cant access; but global keywork help here.

def result():
    res1 = input("enter no: ")
    print(res1)

"""
#result()
#print("res1 value: ",res1)
Traceback (most recent call last):
  File "D:\mydrive\DevopsWorks\PythonWork\functions\scope.py", line 5, in <module>
    print("res1 value: ",res1)
                         ^^^^
NameError: name 'res1' is not defined
"""

def result1():
    global res2
    res2 = input("enter no: ")
    print(res2)

result1()
print("res2 value: ",res2)

"""
enter no: 10
10
res2 value:  10
"""