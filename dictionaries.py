# DICTIONARIES

# "name"(key): "ali"(value)
# "hobbies" : ["cinema", "basketball", "software"]

person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
print(person)
print(person["name"])  # the value of the key we wrote, sena

# element update

person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
print(person)
person["name"] = "senanur"  # only one element changed
print(person)
person.update({"name": "Sena", "age": 30})  # more than one element changed.


# adding

print(person)
person["id"] = 12345  # new key and value added.
print(person)

# delete

del person["id"]  # id element removed.
print(person)

# how to print dics

person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
print(person)

for x in person:  # Only the keys were written
    print(x)

for x in person:  # Values were written.
    print(person[x])

person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
print(person.keys())  # only keys were written.  dict_keys(['name', 'age', 'gender', 'hobbies'])
print(person.values())  # only values. dict_values(['sena', 21, 'f', ['Cinema', 'Concert', 'Software']])
print(person.items())  # both keys and values.


person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
for k in person.items():
    print(k)  # written as:('name', 'sena')..

for k, v in person.items():
    print(k, v)  # written as: name sena..

person = {"name": "sena", "age": 21, "gender": "f", "hobbies": ["Cinema", "Concert", "Software"]}
print(person["id"])  # doesn't exist, KeyError
print(person.get("id"))  # none
print(person.get("name"))  # name exist in dic so : sena
print(person.get("name", "id"))  # sena
print(person.get("id", "Doesn't exists!"))  # If the first parameter doesn't exist ;
                                             # second parameter is the message i want to say.
