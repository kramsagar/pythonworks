#Program to print the given digit in words
#take aways: the dictionary should string key and not supporting int keys. we cant iterate numbers but string.

num = "396"
numbers={
    "0":"zero",
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5": "Five",
    "6": "Six",
    "7":"Seven",
    "8": "Eight",
    "9": "Nine",
}
i=0
numberInWord=""
while i < len(num):
    numberInWord = numberInWord + " " + numbers.__getitem__(num[i])
    i+=1

print("{0} in name format is: {1}".format(num, numberInWord))