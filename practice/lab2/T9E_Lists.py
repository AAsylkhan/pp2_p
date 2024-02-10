'''
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
'''

thislist = ["apple", "banana", "cherry"]
print(thislist)

print(thislist[1]) #List items are indexed and you can access them by referring to the index number

thislist[1:3] = ["blackcurrant", "watermelon"] #Change a Range of Item Values

# The insert() method inserts an item at the specified index
thislist.insert(2, "watermelon")
print(thislist)

#To add an item to the end of the list, use the append() method

thislist.append("orange")
print(thislist)