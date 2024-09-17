#STRING
"""print('merhaba dunya')
print('Ali\'s house')     #\n- >a new line,   #\t-> tab
print("Hello World")
msg = "Hello"
msg2 = "world"
print(msg+" "+msg2)"""

msg = "HelloWorld"
print(msg[0])  #H
print(msg[-1]) #o
print(msg[0:4])  #Hell (first four)
print(msg[1:4]) #ell (starts with 1st index)
print(msg[::2]) #Hloo(go in pairs)
print(msg[::-1]) #dlroWolleH(reverse.)
print(msg.endswith("d")) #true
print(len(msg)) #10
print("Hello" * 5) #10 times "Hello"

name = 'Ali'
age = '20'
print("{},{} years old.".format(name,age)) #Ali 20 years old.
print(f"{name} said {msg}.") #Ali said HelloWorld."""
#print('Merhaba\nDunya')

# INTEGER & FLOAT
# math operators
# "+" "-" "*" "/" "//" "**"
# "abs" "round"

x = 1
y = x
x = 5
print(y)

i = 1
i += 2
print(i) #3

a = 3
b = 3.8
c = 5 ** 100  # power
print(type(b))
print(type(a))
print(c)

print(16 / 3)  # division
print(16 // 3)  # integer division
print(3 ** 4)  # power
print(12 * 32)  # multiplication
print(abs(-3))  # absolute value
print(abs(-3.23))
print(round(abs(-3.23)))  # rounding
a = 22 / 7
print(round(a, 4))

#(),*,/,+,-
print((3 + 2) * 4 + 3)

# comparison operators
# == , > , < , >= , <= , !
num1 = 7
num2 = 10
num3 = 10
print(num1 == num2)
print(num3 == num2)
print(num2 >= num3)
print(num1 < num3)
print(num3 != num2)

#sting to integer
num1 = "100"
print(type(num1)) #str
num2 = 100
print(type(num2)) #int
print(num1 == num2) #false

num3 = int(num1)
print(num3) #100
print(type(num3)) #int
print(num2 == num3) #true

num4 = "100asd"
num5 = int(num4)
print(num5) #valueError

num6 = int(3.6)
print(num6) #3
