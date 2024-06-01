stdList=[1,2]
stdList1=stdList
print(id(stdList) == id(stdList1))
del stdList1[0]
print(id(stdList) == id(stdList1))

stdTuple=(1,3,2)


"""
del stdTuple[0]
Traceback (most recent call last):
  File "d:\mydrive\DevopsWorks\PythonWork\Dict\DictStories.py", line 8, in <module>
    del stdTuple[0]
        ~~~~~~~~^^^
TypeError: 'tuple' object doesn't support item deletion
(.venv) PS D:\mydrive\DevopsWorks\PythonWork> 
"""
#stdTuple.append or stdTuple.insert or sort -> it doesnt support as it is immutable

###################################################################################################

usernames={
    "1":"ram",
    "2":"josh"
}
print(usernames["1"])
print(usernames.items())
print(usernames.keys())
usernames.update({"1":"Chey"})
print(usernames)
usernames1 = usernames.copy()
print(id(usernames) == id(usernames1))

"""
True
True
ram
dict_items([('1', 'ram'), ('2', 'josh')])
dict_keys(['1', '2'])
{'1': 'Chey', '2': 'josh'}
False
"""


