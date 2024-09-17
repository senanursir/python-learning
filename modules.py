#MODULES
"""
import math

result = math.sqrt(12)
print(int(result))
"""

""""
from math import sqrt, factorial
result = sqrt(5)
result2 = factorial(6)
"""

"""
from math import *
result = sqrt(5)
result2 = factorial(6)
"""
# CALLING THE MODULE THAT WE CREATED OURSELVES.
# with function.
"""
import mymodule
result = mymodule.area_circle(4)
print(result)     # 50.24
"""
#
"""
from mymodule import circum_circle
result2 = circum_circle(3)
print(result2)    # 18.84
"""

# with shortcut.

"""
import mymodule as mm

result = mm.area_circle(5)
print(int(result))  #78
"""