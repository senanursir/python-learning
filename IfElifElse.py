# IF ELIF ELSE

a = 5
b = 5
if a == b:
    print("a = b")  # a = b
#

a = 10
b = 5
if a > b:
    print("a > b")  # a > b
#

a = 10
b = 5
if a != b:
    print("a != b")  # a != b
#

a = 6
b = 8
if a == b:
    print("a = b")
else:
    print("a != b")   # a !=b
#

color = "Black"
if color == "White":
    print("White")
elif color == "Yellow":
    print("Yellow")
elif color == "Pink":
    print("Pink")
else:
    print("Black")       # Black


# OR
a = 5
b = 8
c = 10
if a < b or c == a:
    print("it is true!")
else:
    print("it is false!")     # it is true


# AND
a = 5
b = 8
c = 10
if a < b and b == c:         # both condition must be true for it to work
    print("it is true!")
else:
    print("it is false!")  # it is false!

# IN

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 4

if a in list1:
    print("exist")
else:
    print("doesn't exist")   # exist


name = "sena"
a = "b"
if a in name:
    print("exist")
else:
    print("doesn't exist")  # doesn't exist

# NOT
name = "sena"
a = "b"
if not a in name:
    print("exist")
else:
    print("doesn't exist")  # exist

a = 8
b = 10
if not a == b:
    print("true!")
else:
    print("False!")  # true!

#IS

a = "python"
b = "pytho"
b += "n"
# print(a)  -> python
# print(b)  -> python

if a == b:
    print("a = b")
else:
    print("a != b")  # a = b


a = "python"
b = "pytho"
b += "n"

if a is b:
    print("a = b")
else:
    print("a != b")     # a != b
    print(id(a))        # their id value
    print(id(b))        # is different.
                        # they have the same value but they are not the same variable.



