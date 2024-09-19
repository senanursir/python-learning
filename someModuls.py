# RANDOM

import random
# random function
"""
for i in range(10):
    print(random.random())   # random function 10 times (random number between 0 and 1.)
"""

# uniform function
"""
for i in range(10):
    print(random.uniform(1, 20))     # random numbers between 0 and 20
"""

# randint function
"""
for i in range(10):
    print(random.randint(2,30))  # random integer numbers. Both border included(only for this function.)
"""

# randrange function
"""
for i in range(10):
    print(random.randrange(1,10,2))  # 1 to 10, 2 by 2 numbers. available for 2 parameters.
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

dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100):                     # 100 rolls.
    dice = random.randint(1, 6)     # generate numbers from 1 to 6 100 times.
    dices[dice] += 1                     # for ex. 3 is generated: 3:0 turn into 3:1.


for dice in  dices:
    print(f"probability of {dice}: {dices[dice] / 100}")   # probability calculation.




