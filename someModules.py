# RANDOM MODULE

import random
# random function
"""
for i in range(10):
    print(random.random())   # random function 10 times (random number between 0 and 1.)
"""


# uniform function
"""
for i in range(10):
    print(random.uniform(5, 6))     # random numbers between 1 and 20. Both border included.
"""


# randint function
"""
for i in range(10):
    print(random.randint(2,30))  # random integer numbers. Both border included.
"""



# randrange function
"""
for i in range(10):
    print(random.randrange(1,10,2))  # 1 to 9, 2 by 2 numbers. available for 2 parameters.
"""


#choice
""""
list = ["black", "white", "blue", "green", "grey", "orange"]

print(random.choice(list))         # random pick from the list.
"""


# shuffle
"""
list = ["black", "white", "blue", "green", "grey", "orange"]
random.shuffle(list)               # list is mixed
print(list)
"""


# sample
"""
list = ["black", "white", "blue", "green", "grey", "orange"]
print(random.sample(list, 3))        # 3 pick from the list.
"""


# The probability of each face of a die coming up after rolling the die 100 times.
"""
dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100):                     # 100 rolls.
    dice = random.randint(1, 6)     # generate numbers from 1 to 6 100 times.
    dices[dice] += 1                     # for ex. 3 is generated: 3:0 turn into 3:1.


for dice in  dices:
    print(f"probability of {dice}: {dices[dice] / 100}")   # probability calculation.
"""

# How many times were the dice rolled to get 6-6?
"""
six_six = 0
try_n = 0
while True:
    try_n += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 == 6 and dice2 == 6:
        six_six += 1
    if six_six == 10:
        print(f"the dices rolled {try_n} times to get 10 times 6-6. ")
        break
"""

# --------------------------------------------------------------------------------------------------

# TIME MODULE

import time

# TIME.TIME()
zaman = time.time()   # Return the current time in seconds since the Epoch.
print(zaman)

# -------------------------------------------


beginning = time.time()
list = []

for i in range(10000):            # bu işlem ne kadar zaman aldı.
    list.append(i)
ending = time.time()
print(ending - beginning)



# TIME.CTIME()
zaman = time.ctime()           # current time
print(zaman)


zaman2 = time.ctime(10000)     # convert a time in seconds since the Epoch to a string in local time.
print(zaman2)



# TIME.LOCALTIME()
zaman3 = time.localtime()      # time tuple (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
print(zaman3)                  # tm_sec,tm_wday,tm_yday,tm_isdst)

# ----------------------------------------------------

zaman4 = time.localtime(1000)     # seconds since the Epoch to a time tuple expressing local time.
print(zaman4)



# TIME.ASCTIME()
# convert a time tuple to a string. a usable format
# the time tuple is not present, current time as returned by localtime() is used.

zaman = time. asctime()    # current time, Fri Sep 20 11:19:27 2024
print(zaman)


zaman = time.asctime(1000)     # (type error) it has to be 'Tuple or struct_time'.
print(zaman)


zaman2 = time.localtime()
zaman = time.asctime(zaman2)  # conver a time tuple to a string. a usable format: Fri Sep 20 11:27:55 2024
print(zaman)



# TIME.STRFTIME()
# current time with format that we want.

zaman = time.strftime("%d/%m/%Y  %H:%M:%S")  # 20/09/2024  11:35:20
print(zaman)



# TIME.SLEEP()
print("program has been started")
time.sleep(3)                         # delay execution for a given number of seconds
print("program has been ended")
