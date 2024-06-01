try:
    print(Ram)
except:
    print("Error occured")
print("Successfully done!")

###############


try:
    #print(1/0)
    #i = "123"/10
    abc=(1,2);abc.sort()
except ZeroDivisionError:
    print("Division by zero!")
except TypeError:
    print("Formatting issue!")
except:
    print("Unexpected error!")


## heirarchy exceptions: Instead of ZeroDivisionError we can use its parent ArithmaticError to catch all math related errors.