#What is a set in Python?
#   A set is an unordered collection of items. Every elements is unique(no duplicates) and must be immutable (which cannot be changed).

#   However, the set itself is mutable. We can add or remove items from it.
#   Sets can be used to perform mathematical set wperations like union, intersection, symmetric defference etc.

#How to create a set?
#   A set is create by placing all the items(elements) inside curly braces"{}", separated by comma or by using the built-in function "set"
#   It can have any number of items and they may be of different types (integer, float, tuple, string etc.). But a set connot has a mutable 
#   element, like "list".

#set of integer 
set00 = {1, 2, 3}
print(set00)

#set of mixed datatypes
set01 = {1.98, "ohla", (1, 2, 3)}
print(set01)

#set does not have duplicates
set03 = {1,3,5,4,7,8,9,2,4,6,}
print(set03)

#set cannot have mutable items
#set04 = {2, 4, [1, 3]}
#if you uncomment line 25 it gonna be TypeError: unhasshable type: 'list'

#We can make set from a list 
set03 = set([1, 2, 3, 4, 2, 1])
print(set03) 

### Create an empty set is a bit tricky.
#Initialize "book"  with "{}"
book = {}

#check datatype of book 
print(type(book))   # It's not set datatype it gonna be dictionary 

#if you want to create empty set to store in valaible you have to do following steep

book = set()
print(type(book))   # This is a set datatype


#---------------------------------------------------------------------------------------------------------------------------------------------#


# How to change a set in python?
#   We cannot access or change an element using the "add()" methond and multiple elements using the "Update() method. The "update()" can take
#   tuples, lists, string or other sets as it argument. in all cases, duplicates are avoided.

#if you uncomment line 55 you will get TypeError: 'set' object does not support indexing.

#set00[0] 

#add an element 
set00.add(-1)
print(set00)

#add multiple elements using "update()"
set00.update([0, -2, 1, 3])
print(set00)

#add list and other set to set00
set00.update([4, 6], {7, 5, 0}, ("Sets"))
print(set00)




