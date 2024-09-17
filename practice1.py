# INPUT

number = input("Enter a number: ") # get value from the user.

print(number)         # 12
print(type(number))   # <class 'str'>
number = int(number)   # turned into a integer.
print(type(number))   # <class 'int'>  or:

numbers = int(input("Enter a number: "))
print(type(numbers))



# CALCULATE THE NUMBER OF A NUMBER TAKING FROM THE USER.

# WITH FOR

number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):  # +1 cause second one is not including.
    factorial *= i

print(f"{number}! = {factorial}")   # 5! = 120



# WITH WHILE

number = int(input("Enter a number: "))

factorial = 1
i = 2

while i <= number:
    factorial *= i
    i += 1

print(f"{number}! = {factorial}")



# WRITE A PROGRAM THAT CHECKS WHETHER A NUMBER TAKEN FROM THE SCREEN IS PRIME.

number = int(input("enter a number "))

prime = True

for i in range(2, number):   # 1 and the number itself cannot be included.(The number is accepted as non-prime in any case)
    if number % i == 0:
        prime = False
        break
if prime == True:
    print(f"{number} is a prime number ")
else:
    print(f"{number} isn't a prime number ")



# HOW MANY POSITIVE DIVISORS DOES THE NUMBER TAKEN FROM THE SCREEN HAVE?

number = int(input("enter a number "))

divisor_number = 0
for i in range(1, number + 1):
    if number % i == 0:
        divisor_number += 1

print(f"{number} has {divisor_number} divisor.")  # 12 has 6 divisor.



# THE SUM OF THE DIGITS OF A NUMBER TAKEN FROM THE USER.

# by converting the number to a string.

number = int(input("enter a number "))  #123456789

str_num = str(number)   # the number turned into a string.
sum = 0
for digit in str_num:   # digit is string(part of the str_num
    sum += int(digit)   # digit turned into a int.

print(sum)          # 45



# without converting the number to a string.

number = int(input("enter a number "))

sum = 0
temporary_num = number

while temporary_num != 0:
    digit = temporary_num % 10
    sum += digit
    temporary_num //= 10

print(sum)



# WRITE A PROGRAM THAT PRINTS THE SMALLEST AND ARGEST OF THE 5 NUMBERS TAKEN FROM THE USER.

list = []
for i in range(5):
    number = int(input("Please enter a number: "))  # Numbers were entered 5 times and these numbers were added to the list.
    list.append(number)

print(f"Bigger number is {max(list)}")
print(f"Bigger number is {min(list)}")



# CHECK IF A NUMBER TAKEN FROM THE USER IS A SQUARE NUMBER.

number = int(input("enter a number "))
square_root = number ** 0.5
if square_root == int(square_root):   # if it's integer then it's a square number.
   print("Square number.")

else:
    print("Not a square number.")
    print(square_root)


# TO DETERMINE WHICH LETTER IS USED HOW MANY TIMES IN THE TEXT TAKEN FROM THE USER.

text = input("enter a text: ")   #senanur
dict1 = dict()
for letter in text:
    if letter in dict1:
        dict1[letter] += 1
    else:
        dict1[letter] = 1

for letter, how_many in dict1.items():
    print(letter, how_many)             #s1,e1,n2,a1,u1,r,1



# CAPITALIZING THE LETTERS A IN THE TEXT TAKING FROM THE USER.

text = input("enter a text: ")    # akbaba
text2 = ""

for letter in text:
    if letter == "a":
        text2 += "A"
    else:
        text2 += letter   # added normally(for example letter k)
print(text2)                 # AkbAbA




