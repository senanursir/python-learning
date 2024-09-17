
# HOW MANY OF THE FIRST 10,000 PRIMES START WITH 3 AND END WITH 7?
"""
prime_list = list() # created an empty list.
prime_list.append(2) # 2 error solving.

number = 3  # starts with 3.
while True:
    prime = True
    for i in range(2, int(number ** 0.5) + 1 ):   # i variable from 2 to square root of the number (optimization.)
        if number %i == 0:       # If our number is divided by the variable without remainder.
            prime = False        # not prime.
            break                # stop
    if prime:
        prime_list.append(number)   # if prime = true number added to the list
        if len(prime_list) == 10000:  # if the list's length 10000
            break                     # stop
    number += 1                       # the next number.

print(prime_list)      # 10000 prime number.


# starts with 3 - ends with 7 control.
list2 = []
for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
       list2.append(prime)

print(list2)
print(len(list2))   # 270
"""



# HOW MANY OF THE THREE-DIGIT NUMBERS ARE EQUAL TO THE SUM OF THE CUBES OF THEIR DIGITS.
"""
list = []
for num in range(100, 1000):   # number from 100 to 999.                          145,146,147...
    sum = 0                                                                     # 125, 189...
    temp_num = num             # temporary number for individual digit control.   145, 14, 1
    while temp_num != 0:        # 0 control!
        digit = temp_num % 10   # units digit taken.                              5 -> digit          4-> digit
        sum += digit ** 3   # cube of the digit added to sum.                     5^3 = 125 -> toplam 4^3 -> toplam
        temp_num //= 10     # for the next digit.                                 145/10 = 14         14/10 = 1
    if sum == num:
        list.append(num)    # added to sum.

print(list)         # [153, 370, 371, 407]
print(len(list))    # 4
"""



# FIRST 100 FIBONACCI NUMBERS.
# WITH WHILE
"""
fibonnacci_list = []
fibonnacci_list.append(1)
fibonnacci_list.append(1)

index = 2

while True:
    fibonnacci_list.append(fibonnacci_list[index - 2] + fibonnacci_list[index - 1])
    index += 1
    if len(fibonnacci_list) == 100:
        break
        
print(fibonnacci_list)
"""

# WITH FOR
"""
fibonnacci_list = []
fibonnacci_list.append(1)
fibonnacci_list.append(1)

for i in range(2, 100):    #2. to 99.
    fibonnacci_list.append(fibonnacci_list[i - 2] + fibonnacci_list[i - 1])

print(fibonnacci_list)

"""



# PRINT THE FIRST 100-DIGIT FIBONACCI NUMBER ON THE SCREEN
"""
fibonnacci_list = []
fibonnacci_list.append(1)
fibonnacci_list.append(1)

index = 2

while True:
    fibonnacci_list.append(fibonnacci_list[index - 2] + fibonnacci_list[index - 1])  # Add the two preceding terms.
    term = fibonnacci_list[index - 2] + fibonnacci_list[index - 1]                   # assign to the variable term
    if len(str(term)) == 100:                                                        # if number of digits of the term
        print(term)                                                                  # print
        print(index)
        break
    index += 1
    
"""






