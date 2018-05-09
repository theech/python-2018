#There are various ways in which we can access the elements of tuple.

#Indexing
#We can use the index operator [] to access an item in a tuple where the index started from 0.
#So, a tuple having six elements will have index from 0 - 5. Trying to access an element other that (6,7,...) will raise an IndexError.
#The index must be an integer, so we cannot use float or other types. This will result into TypeError.
#Likewise, nested tuple are accessed using nested indexing, as shown in the example below.

items00 = ('p', 'e', 'r', 'm', 'i', 't')

print(items00[0])
print(items00[5])

#index must be in range, if you uncomment line 17. You will get an Error.
#IndexError: tuple index out of range.

#print(items00[6])



#index must be an integer. if you uncomment line 24. You will get an Error.
#TypeError: tuple indices must be integers, not float.

#print(items00[2.7])



#nested tuple 
items01 = ("imagine", [2, 4, 78], [1.2, 65.4, 543.5, 0.45])
print(items01[0][3])
print(items01[1][2])
print(items01[2][3])

#-------------------------------------------------------------------------------------------------------------------------------------------#

#Nagative indexing
#Python allows nagative indexing for its sequences. 
#The index of -1 refers to the last item, -2 to the second last item and so on.

print(items00[-1])
print(items01[-2])

#-------------------------------------------------------------------------------------------------------------------------------------------#

#Slicing 
#we can access a range of items in a tuple by using the slicing operator - colon ":"

items02 = ('P', 'R', 'O', 'G', 'R', 'A', 'M', 'M', 'I', 'N', 'G')

#elements 2nd to 4th
print(items02[1:4])

#elements beginning to 2nd
print(items02[:-7])

#elements 8th to end 
print(items02[7:])

#element beginning to end
print(items02[:])


#slicing can be best visualized be consdering the index to be between the elements as shown below. So if we wan to access a range, we need the
#index that will slice the portion from the tuple.
#    | P | R | O | G | R | A | M | M | I | N | G |
#    0   1   2   3   4   5   6   7   8   9   10  11
#    -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  



#-----------------------------------------------------------------------------------------------------------------------------------------#

#Changing a tuple 
#Unlike lists, tuples are immutable
#This means that elements of a tuple cannot be changed once it has been assigned. But, if the element is itself a mutable datatype like list
#its mested items can be channged. 
#We can also assign a tuple to different valuses (reassignment).

items03 = (2,4,3,[6,5])

#we can not change an elements
#if you un comment line 85
#you will get TypeError: 'tuple' object does not support item assignment.

#items03[1] = 9

#but, item of mutable element can be changed

items03[3][0] = 9
print(items03)

#we can use + operator to combine two tuple. This also called concatenation

print((1,2,3,4) + (5,6))

#we can also repeat the elements in a tuple for a given number of times using the * operator.

print(("Repeat", "tuple",) * 3)

#----------------------------------------------------------------------------------------------------------------------------------------------#

#Deleting a tuple 
#As discussed above, we can not change the elements in tuple. that also mean wee cannot delete or remove items from a tuple 

#cannot delete items
#if you uncomment line 109
#you will get an error TypeError: 'tuple' object does not support item deletion

#del items03[2]

#but we can delete intire tuple 
#if you uncomment line 144 you will get -> NameError; name 'items03' is not defined
del items03
#items03

#---------------------------------------------------------------------------------------------------------------------------------------------#

#Python Tuple Methods : Methods that add items or remove items are not available with tuple. Only the following two methods are available.
#           | Method   |                 Description                    |
#           | count(x) | Return the number of items that is equal to x  |
#           | index(x) | Return index of first items that is equat to x |

items04 = ('a', 'p', 'p', 'l', 'e', 2, 4, 7,7,7,78)

#count method
print(items04.count('l'))
print(items04.count(7))

#index method 
print(items04.index(4))
print(items04.index('a'))


#--------------------------------------------------------------------------------------------------------------------------------------------#
#other tuple operations
# 1. Tuple membership test
# We can test if an item exists in a tuple or not, using the keyword "in".
#check "e" in tuple 
print('e' in items04)
print('f' in items04)

print(5 not in items04)
print('p' not in items04)

# 2. Iterating through a tuple
# Using  a 'for' loop ce can though each item in a tuple

for nam in ("NoOne", "NoNeed"): 
    print("Hello", nam)

# 3. Built-in Function with Tuple : 
# Built-in function like : all(), any(), enumerate(), len(), max(), min(), sorted(), tuple() etc are commonly used with tuple to perform
# different tasks. link : https://www.programiz.com/python-programming/tuple 
 


