#We can access individual characters using indexing and a range of characters using slicing.
#Index start form 0. Trying to access a character out of index range will raise an "IndexError. The index must be an integer. We can not use
#float or other tupes, this will result in "TypeError.

#Python allows negative indexing for its sequences.

#The index of -1 refers to the last item, -2 to the second last item and so on. We can access a range of items in a string by using the slicing
#operator (colon)

string = 'gunman'
print('str = ', string)

#first character
print('str[0]', string[0])

#last character 
print('str[-1]', string[-1])

#slicing 2nd to 5th character
print('str[1:5]', string[1:5])

#slicing 3rd to last second charater
print('str[2:-2]', string[2:-2])

#last item 
print('str[-1]', string[-1])


#---------------------------------------------------------------------------------------------------------------------------------------# 
#If we access index out of the range or use decimal number (not integer) will get errors.

#index is must be in range
#You will get : "IndexError: string index out of range"
string[20]

#index must be an integer
#You will ger : "TypeError: string index must be integers, not float"
string[4.1]

#Slicing can be best visualized by considering the index to be between the elements as shown below.
#If you want to access the range, we need the index will slice the portion from the string.

#   | G | U | N | M | A | N |
#   0   1   2   3   4   5   6
#   -6  -5  -4  -3  -2  -1 


