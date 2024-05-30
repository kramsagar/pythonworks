a=22 #0b10110
b=23 #0b10111
print(bin(a))
print(bin(b))
c = bin(a & b) ;print(c) #bit wise and
d = bin(a | b) ;print(d) #bit wise or
e = bin(a ^ b) ;print(e) #exclusive or
f = ~a
print(f)

print(a >> 1)  #shift right
print(int(0b01011))
print(a >> 2)  #shift right
print(int(0b00101))

print(a << 1)  #shift left
print(int(0b101100))
print(a << 2)  #shift left
print(int(0b1011000))


"""
0b10110
0b10111
0b10110
0b10111
0b1
-23
11
11
5
5
44
44
88
88
"""

