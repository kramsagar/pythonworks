def print_sum(num1,num2):
    print("The given numbers {0} and {1}".format(num1,num2))
    sum1 = num1 + num2
    if(sum1 == 0):
        return
    print("the sum is ",sum1)

print_sum(100,200)
print_sum(100,-100)