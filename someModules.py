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

for i in range(10000):            # How much time did this process take.
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


# --------------------------------------------------------------------------------------------------
# DATETIME MODULE

# DATE

from datetime import date

bugun = date.today()
print(bugun)
print(type(bugun))      # class
print(bugun.day)        # only day, 21
print(bugun.year)
print(bugun.month)
print(bugun.weekday())     # monday's index number is 0
print(bugun.isoweekday())  # monday is 1.


bugun = date.today()
date1 = date(2003,8,4)

print(date1.weekday())                     # it was monday(index 0)
print(bugun-date1)                         # 7719 days, 0:00:00     , timedelta


# -----------------------------------------
# DATETIME

from datetime import datetime

suan = datetime.now()                     # 2024-09-21 19:00:10.785030
print(suan)
print(type(suan))                         # <class 'datetime.datetime'>
print(suan.year)
print(suan.month)
print(suan.day)
print(suan.hour)
print(suan.minute)
print(suan.second)

print(suan.ctime())                       # Sat Sep 21 19:03:23 2024
print(suan.date())                        # only date part of suan


# -------------------


suan = datetime.now()

pastdate = datetime(2022, 3, 15, 11, 5, 12, 123)

print(suan - pastdate)                     # 921 days, 8:06:20.399859


# -------------------


bugun = date.today()
suan = datetime.now()

# strftime
# how we want to print date from bugun - suan

print(bugun.strftime("%d/%m/%Y"))         # 21/09/2024
print(suan.strftime("%d/%m/%Y"))          # 21/09/2024

print(bugun.strftime("%d/%m/%Y %A"))         # 21/09/2024 Saturday
print(suan.strftime("%d/%m/%Y-%A"))          # 21/09/2024-Saturday

# another usage
print(date.strftime(bugun, "%d/%m/%Y %A"))            # 21/09/2024 Saturday


# -----------------------------------------
# TIMEDELTA

from datetime import timedelta
suan = datetime.now()
tdelta = timedelta(days=7, hours=5, seconds=59)
print(suan + tdelta)                       # After that time from the time we were in?: 2024-09-29 00:27:51.282504
print(suan - tdelta)                       # önce: 2024-09-14 14:25:53.282504


# -----------------------------------------
# PROBLEM SOLVING
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import datetime

sundays = 0
for year in range(1901, 2001):
    for moth in range(1, 13):                               # after the 12 months are over, it moves on to the next year
        if datetime(year, moth, 1).weekday() == 6:     # checks if first of the month is monday
            sundays += 1
print(sundays)         # 171








