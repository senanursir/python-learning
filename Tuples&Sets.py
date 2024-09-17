#TUPLES&SETS
#TUPLES ()
tuple = ("Yellow", "Blue", "Green", "Red", "Black") #!normal parentheses
print(type(tuple)) #tuple
print(len(tuple)) #5
print(tuple)

for color in tuple:
    print(color) #Unlike lists, in tuples, elements cannot be changed, added or deleted.

#SETS {}
#unordred, Unique element

set = {"Yellow", "Blue", "Green", "Red", "Black"}
print(type(set)) #tuple
print(len(set)) #5
print(set)

for colors in set:
    print(colors) #Different order each time

##

set = {"Yellow", "Blue", "Green", "Red", "Black"}
print(set)
set.add("Pink")
set.remove("Blue")#blue get removed
set.discard("Blue")#blue get removed
set.remove("grey")#keyerror
set.discard("grey") #we wanted to remove grey(which doesn't exist) but it didn't give an erros
print(set)

##

set1 = {"Yellow", "Blue", "Green", "Red", "Black"}
set2 = {"Yellow", "Blue", "Green", "White", "Grey"}
print(set1.intersection(set2)) #common elements #intersection
print(set2.intersection(set1)) #same
print(set1.union(set2)) #all elements
print(set1.difference(set2)) #exist in set 1 but doesn't exist in set2
print(set2.difference(set1)) #exist in set 2 but doesn't exist in set1

##

set1 = {"Yellow", "Blue", "Green", "Red", "Black"}
set2 = {"Yellow", "Blue", "Green", "White", "Grey"}
print("Yellow" in set1) #is yellow exist in set1? /true
print("White" in set1) #false
print("White" in set1.union(set2)) #true

##

#creates an empty list
emptytlist1 = []
emptylist2 = list()

#creates an empty tuple
emptytuple1 = ()
emptytuple2 = tuple()
print(type(emptytuple2))

#first one creates an empty set
emptyset1 = set()
emptyset2 = {} #its a dictionary
print(type(emptyset2)) #<class 'dict'>

##

python =set("PYTHON") #list
print(python) #{'O', 'Y', 'N', 'T', 'H', 'P'} Elements separated

python =set([1,2,3,4,5]) #list
print(python)     #turned into a set, {1, 2, 3, 4, 5}

python =set((1,2,3,4,5)) #tuples
print(python)     # #turned into a set, {1, 2, 3, 4, 5}

#

