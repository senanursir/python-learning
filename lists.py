colors=["green", "blue", "purple", "white", "black"]
#print(type(colors))
#print(colors)
print(len(colors))#how many
print(colors[1]) #blue
print(colors[0])#green
print(colors[6])#index error
print(colors[1:4])#1st to 4th
print(colors[:4]) #first four
print(colors[::2])#go in pairs
print(colors[1:4:2]) #starts with 1st and then goes in pairs


#append method
#insert method
#remove method
#extend method
#pop method
#reverse method
#sort and sorted method

colors=["green", "blue", "purple", "white", "black"]
print(colors)
colors.append("grey")
print(colors)
##
colors=["green", "blue", "purple", "white", "black"]
colors.insert(2,"pink")#added pink as a 2nd index
print(colors)
##
colors=["green", "blue", "purple", "white", "black"]
print(colors)
colors.append("grey")
print(colors)
colors.insert(2,"pink")#added pink as a 2nd index
print(colors) #grren,blue,pink,purple,white,black,grey
##
colors2 = ["green", "yellow", "purple",]
colors.remove("yellow") #removed yellow
print(colors)
##
colors1 = ["green", "blue", "pink", "grey", "black"]
colors2 = ["green", "yellow", "purple"]
colors1.append(colors2) #list2 added to list1 as a list
print(colors1)
##
colors1 = ["green", "blue", "pink", "grey", "black"]
colors2 = ["green", "yellow", "purple"]
colors1.extend(colors2) #list2's object added to list1
print(colors1)
##
colors = ["green", "blue", "pink", "grey", "black"]
colors.pop() #last one removed
print(colors)
##
deleted = colors.pop() #assigned
print(deleted) #says which one is deleted
##
colors = ["green", "blue", "pink", "grey", "black"]
print(colors)
colors.reverse() #sorted reverse
print(colors)
##
colors = ["green", "blue", "pink", "grey", "black"]
print(colors)
colors.sorted() #sorted , alphabetical order if there are textual expressions in it
print(colors)   #aFrom small to large order if there are numerical expressions in it
##
colors = ["green", "blue", "pink", "grey", "black"]
colors.sort(reverse = True) #Reversed order
print(colors)

##
colors = ["green", "blue", "pink", "grey", "black"]
print(colors)
##
liste2=sorted(colors)
print(liste2)  #sorted without changeing the original list.
print(colors)
##

colors = ["green", "blue", "pink", "grey", "black"]
numbers = [1, 23, 12,6,30,11]

print(max(colors)) #at the end alphabetically
print(max(numbers)) #Largest number
print(sum(numbers)) #sum
#print(sum(colors)) #typeError
##

for i in colors:
    print(i)  #one by one colors
##

colors = ["green", "blue", "pink", "grey", "black"]
print(list(enumerate(colors))) #Colors numbered

colors = ["green", "blue", "pink", "grey", "black"]
print(list(enumerate(colors,start = 3))) #Colors numbered starting from 3
##
#in
colors = ["green", "blue", "pink", "grey", "black"]
print("blue" in colors) #is blue on the list?
print(colors )  #true
##
#list to string -join

colors = ["green", "blue", "pink", "grey", "black"]
stringcolors = ",".join(colors)
print(stringcolors)   #color with "," (green,blue, pink,grey,black)

colors2 =stringcolors.split(",")
print(colors2)