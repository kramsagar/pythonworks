age=100
if age < 110:
    print("Age is more than 100",age)
elif age == 100:
    print("Age is equal to 100",age)
else:
    print("not")

"""
loops
"""
i=0
while i < 5:
    print("while inside while loop",i)
    i+=1
else:
    print("while exiting finally",i)

"""
loops
"""

for i in range(11):
    if i % 2 == 0:
        print("for this is even",i)
        continue;
    print("for this is odd",i)
    if i % 9 == 0:
        break;
else:
    print("for exited from for loop",i)

"""
for this is even 0
for this is odd 1
for this is even 2
for this is odd 3
for this is even 4
for this is odd 5
for this is even 6
for this is odd 7
for this is even 8
for this is odd 9
==================================
for this is even 0
for this is odd 1
for this is even 2
for this is odd 3
for this is even 4
for this is odd 5
for this is even 6
for this is odd 7
for this is even 8
for this is odd 9
for this is even 10
for exited from for loop 10
"""