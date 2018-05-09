# Python String Operations

# There are many operations that can be performed with string which makes it one of the most used. 

# 1. Concatenation of Two or More Strings
#       Joining of two or more strings into a single one is called concatenation. 
#The + operator does this Python. Simply writing two string literals together also concatenates them. The 
#The * operator can be used to repeat the string for a given number of times.

string00 = "Hello " 
string01 = ' World!'

#using +
print('string00 + string01', string00 + string01)

#using *

print(string00 * 3)





#writing two string leterals together also concatenates them like + operator. If we want to concatenate string indefferent lines, we can
# parentheses.

#two string literals together
print("Hello" "world!")

#using parentheses
string02 = ("Hello" 
                " World "

                "I am different person"
            )
print(string02)


#---------------------------------------------------------------------------------------------------------------------------------------------#
# 2. Iterating Through String 
#       Using for loop we can iterate through a string. Here is an example to count the number of "e" in a string. 
count = 0 

for letter in string02:
    if letter is 'e':
        count += 1

print("There are ", count, "in a string02") 



#--------------------------------------------------------------------------------------------------------------------------------------------#
# 3. String Membership Test
#       We can test if a sub string exists a string or not, using the keyword "in"

letterCheck = 'L'
checkStringMember = letterCheck in string02

if checkStringMember is True:
    print("It's ", letterCheck," in string02")

else:
    print("It's not ", letterCheck, " in string02")



#--------------------------------------------------------------------------------------------------------------------------------------------#
# 4. Built-in function to Work with Python
#       Various buit-in fucntion work with sequence, work with string as well.

#       Some of the commontly use once are "enumerate()" and "len()". The "enumerate()" fucntion are returns an enumerate object. it contains the
#       the index and value of all the items in the string as pairs. This can be useful for iteration 
#       Similarly, "len()" retruns the length (number of characters) of the string.

string03 = "cool one"

#enumerate()
ListEnumerate = list(enumerate(string03))
print('lest(enumerate(string03)) = ', ListEnumerate)

#character count using "len()" fucntion
print('len(stirng03 = ', len(string03))





