# FUNCTIONS

"""
def info():
    print("procces successful ")
    print("inside of the function!")

info()
"""

# With parameter
"""
def say_hi(name):
    print("Hi " + name)

say_hi("sena")              #hi sena
"""
#

"""

def topla(x, y):
    print(f"x+y= {x+ y}")

topla(3,4)
"""


# using with lists.
"""
def calc_avg(list):
    sum = sum(list)
    amount = len(list)               # methods of lists were used.
    avg = sum / amount
    print(f"average of the numbers: {avg}")


calc_avg([1, 2, 3, 4, 5, 6, 7])  # 4.0  # liste girilmeli.
"""


# using with methods
"""
def turn_into_upper_case(txt):
    txt = metin.upper()   # methods of strings.
    print(txt)

turn_into_upper_case("senanur sır")  # has to be string
"""


#
"""
def say_hi(mesaj,name= "anonymous"):    # 2nd one is optional.
    print(f"{mesaj}, {name}.")

say_hi("merhaba","elif")    # 2nd parameter doesn't exist, default one is used
"""


#
"""
def make_dis(price, percent = 20):
    amountof_dis = price * (percent / 100)
    new_price = price - amountof_dis
    print(f"Price with discount: {new_price}")


make_dis(100)     # Price with discount: 80.0
"""


# return
# we must use 'return' so that we can assign it to a variable and call it again.
"""
def sum(x, y):
    print(x + y)
    return x+ y             # returns the value.

result = sum(3,4)     
print(result)
"""


# another usage
"""
def calculate_avg(x, y):
    return (x + y) / 2

print(calculate_avg(3, 7))  # 5
"""


#
"""
def calculate_avg(x, y):
    return (x + y) / 2

print(type(calculate_avg))            # <class 'function'>
print(type(calculate_avg(2,6)))       # <class 'float'>

a = calculate_avg(2, 6)
b = calculate_avg(3, 11)
print(a + b)
"""

# assign to a variable
"""
def turn_into_upper(smt):
    return smt.upper()

a = turn_into_upper("welcome to nigde.")
print(a)
"""

# functions can also be equated to a variable.
"""
def turn_into_upper(smt):
    return smt.upper()

fonk = turn_into_upper
sonuc = fonk("thank you ^^ ")
print(sonuc)           #THANK YOU ^^
"""