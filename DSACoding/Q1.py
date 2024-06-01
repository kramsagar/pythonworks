#Count number of even and odd elements in an array
a = [1,2,3,4,5]
even_counter=0
odd_counter=0
for i in a:
    if i%2==0:
        even_counter+=1
    else:
        odd_counter+=1
print("Total no of even numbers are {0} and odd numbers are {1}".format(even_counter,odd_counter))