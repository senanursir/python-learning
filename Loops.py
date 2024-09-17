# LOOPS(FOR AND WHİLE)

# FOR
# We can use "for" loop in tuples, strings and lists.

list1 = ["a", "b", "c", "d", "e"]
for i in list1:
    print(i)  # abcde printed top to the bottom.

##

tuple1 = (1, 2, 3, 4, 5)
for i in tuple1:
    print(i)   # 12345 printed top to the bottom.

##

name = "se@na"
for i in name:
    print(i)      # sena printed top to the bottom.


name = {1, 2, 3, 4, 5}
for i in name:     # also a set.?
    print(i)

# RANGE

for i in range(0, 10):
    print(i)               # printed from 0 to 9. first one including, second one is not


for i in range(1, 17, 2):
    print(i)               # it was printed from 1 to 16, two by two.

# If the first one is not written, 0 is assumed by default

result = 1
for i in range(0, 10):
    result *= 2
print(result)            # 1024 (2^10)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for letter in list1:
    for number in list2:
        print(letter, number)   # printed as : a1, a2, a3, b1, ....c3

#BREAK and CONTINUE
list = [1, 2, 3, 4, 5]
for i in list:
    if i == 3:
        #print("we passed 3")  # cause it is saying to continue
        continue              # 3 isn't printed.
    print(i)                  #1, 2, 4, 5


list = [1, 2, 3, 4, 5]
for i in list:
    if i == 3:
        break              # loop has stopped : 1, 2
    print(i)

#


liste = range(100)

for i in liste:
    if i % 3 != 0:
        continue
    if i == 81:          # Numbers divisible by 3 up to 81
        break
    print(i)
##


# WHILE
x = 1
while x < 10:
    print(x)
    x += 1         # printed 1 to 9.

##

x = 2
y = 3
while x * y < 1000:
    print(x, y)           # (x, y) printed (2,3) to (30,31)
    x += 2
    y += 2

##

i = 1
while True:
    print(i)
    i += 1  # endless loop.

#

i = 1
while True:
    print(i)
    i += 1
    if i == 1000:
        break         # 1 to 999.

i = 1        # odd numbers 1 to 999
while True:
    if i % 2 == 0:
        i += 1
        continue       # Even numbers continue the loop
    print(i)
    i += 1             # odd numbers are printed
    if i == 1000:      # to 1000
        break
