# How to remove elements from a set?
#   A particular item can be removed from set using methods, "discard()" and "remove()". The only defferent between them is that, while using 
#   "discard()" if the item does not exist in the set, it remains unchanged. But "remove()" will raise error in such condition.

#initialize set
set00 = {1,2,3,4,5,6}
print(set00)

#discard an element 
set00.discard(4)
print(set00)

#remove an element
set00.remove(2)
print(set00)

#discard an element not pressent in set00
set00.discard(7)
print(set00)

#remove an element not pressent in set00
#set00.remove(7)

#if you uncomment line 22 you will get KeyError: 7


#we can remove and return an item using the "pop()" method. Set being unordered, there is no way of determining which item will be popped.
#It is completely arbitrary. 

#we cam remove all items from set by using "clear()" method.

set01 = set("HelloWorld")
print(set01)

#pop an element 
print(set01.pop())

set02 = set01.pop()
print(set02)            #it will random element to print out.

#clear an set01
set03 = set01.clear()
print(set03)






