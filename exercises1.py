# mission1:

x = 8
y = 3.5
z = 8j + 9
a = "hello world"
b = True
c = 22 < 20
k = [1, 2, 3, 4, 5]

d = {"name": "jake",
     "age": 27,
     "address": "downtown"}

t = ("machine learning", "data science",)
v = {"machine learning", "data science", "python"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(k))
print(type(d))
print(type(t))
print(type(v))



# mission2:


# ['THE', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

text = "The is to turn data into information, and information into insight. "
text = text.replace(".", " ").replace(",", " ").upper()
text= text.split()
print(text)

# ['THE', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']



# mission3:


lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

print(len(lst))  # 11
print(lst[0], lst[10]) # D E

sublist = lst[0:4]
print(sublist)      # ['D', 'A', 'T', 'A']

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
lst2 = lst.pop(8)
print(lst)            # ["D", "A", "T", "A", "S", "C", "I", "E", "C", "E"]

lst.append("R")
print(lst)      # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 'R']

lst.insert(8, "N")
print(lst)    # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 'R']



# mission 4:


dict1 = {'Christian': ["America", 18],
        'Daisy': ["England", 121],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 251]}
# keys:
for x in dict1:
    print(x)

print(dict1.keys())

# values:
print(dict1.values())

# update:
dict1.update({'Daisy': ["England", 13]})
print(dict1)
# dict1["Daisy"] = 12

# adding:
dict1["Ahmet"] = ["Turkey", 24]
print(dict1)

# delete:
del dict1["Antonio"]
print(dict1)



# mission 5:


a = [2, 13, 18, 93, 22]

def func1(liste):
    even_list = []
    odd_list = []
    for number in liste:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return even_list, odd_list

even_list, odd_list = func1(a)

print(even_list, odd_list)  # [2, 18, 22] [13, 93]



# mission 5:


ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for i, ogrenci in enumerate(ogrenciler):
    if i < 3:
        print(f"Muhendislik Fakultesi:{i + 1} Öğrenci:" + ogrenci)
    else:
        print(f"Tıp Fakultesi:{i - 2} Öğrenci:" + ogrenci)



# mission 7:


ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204" ]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 251]

for a, b, c in zip(ders_kodu, kredi, kontenjan):
    print(f" Kredisi {b} olan {a} kodlu dersin kontenjanı {c} kişidir.") 



# mission 8:

"""
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kumeler():
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

kumeler()
"""