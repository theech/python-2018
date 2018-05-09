#in python programming, a tuple is smilar to a list. The difference between the
#two is that we cannot change the elements of a tuple once it is assigned
#whereas in a list, elements can be changed. 

#Creating a Tuple : A tuple create by placing all the items (elements) inside a
#parentheses(), separated by comma. The parentheses are optional but is a good
#practice to write it'

#A tuple can have any number of items and they may be of defferent types
#(integer, float, list, string, etc,).


#empty tuple 
items00 = ()
print(items00)


#tuple having integer
items01 = (12, 23, 34, 45)
print(items01)

#tuple that mixed datatypes (integer and string and float)
items02 = (11, 23.4, "hello")
print(items02)

#nested tuple 
items03 = ("hi", [1, 2, 3], [1.0, 2.0, 3.0])
print(items03)

#tuple can be create without parentheses
#also called tuple packing
items04 = 1, 3.3, "Halliwood"
print(items04)

#tuple unpacking is also possible 
a, b, c = items04
print(a)
print(b)
print(c)

#--------------------------------------------------------------------#
#creating a tuple with one element is a bit tricky
#Having one element within parentheses is not enough. 
#We will need a trailing comma to indicate that it is in fact a tuple.

items05 = ("hello")
print(type(items05))

#need a comma at the end
items06 = ("hello",)
print(type(items06))

#parentheses is optional
items07 = "hello",
print(type(items07))

