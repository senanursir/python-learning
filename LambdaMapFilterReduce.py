# LAMBDA, MAP, FİLTER, REDUCE

# lambda a, b: a+b

salaries = [1000, 2000, 3000,4000]

print(list(map(lambda x: x * 20 / 100 + x, salaries)))
# [1200.0, 2400.0, 3600.0, 4800.0]

print(list(map(lambda x: x ** 2, salaries)))

list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x % 2 == 0, list_store)))
# [2, 4, 6, 8]

from functools import reduce
listb = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b,listb))
# 10




