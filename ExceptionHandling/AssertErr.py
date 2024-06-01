"""
i = int(input("read details"))
assert i > 0

read details-1
Traceback (most recent call last):
  File "D:\mydrive\DevopsWorks\PythonWork\ExceptionHandling\AssertErr.py", line 2, in <module>
    assert i > 0
           ^^^^^
AssertionError
"""


def readdetails():
    try:
        i = int(input("read details"))
        i / 0
    except:
        raise
try:
    readdetails()
except:
    print("unexpeccted error")
    
"""
read details10
unexpeccted error
"""

"""
Assert error for pre and post checks purpose.
Exceptions are unexpected flow execution error to catch
"""