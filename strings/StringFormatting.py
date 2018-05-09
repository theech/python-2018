# Python String Formatting
# 1. Escape Sequence
#       If we want to print a text like -He said, "Who are You man?" -we can niether use single quote or double quotes. This will result in to 
#       "SyntaxError" as the text itself contains both single and double quotes.

#print("He said, "Who are you man"")

#If you uncomment line 6 you will get an error.
#"SyntaxError: invalid syntax"

#There are three way to get around this proble are showing bellow.

#Using triple quotes
print('''He said, "Who are you man?" ''')

#Using escaping single quotes.
print('He said, "Who\'re you man?"')

#Using escaping duoble cuotes
print("He said, \"Who're you man\" man?")

#Here is a list of all the escape sequence support by python.

#           Escape Sequence                     Description
#           \newline            |       Backslash and new line ignored
#           \\                  |       Backslash
#           \'                  |       Single quote
#           \"                  |       Double quote
#           \a                  |       ASCII Bell
#           \b                  |       ASCII Backspace
#           \f                  |       ASCII Formfeed
#           \n                  |       ASCII Linefeed
#           \r                  |       ASCII Carriage return
#           \t                  |       ASCII Horizontal Tab
#           \v                  |       ASCII Vertical Tab
#           \ooo                |       Character with octal value ooo
#           \xHH                |       Character with hexadecimal value HH


#Here are some examples

print("Script\\Python\\programiz\\strings")

print("Seperate in two line \n you can use \\n")

print("This is \x48\x49\x50 representatioin")

print("\t The one you don't wanna know")

print("\v Be Youself then you gonna be awesome")


#------------------------------------------------------------------------------------------------------------------------------------------#

#   2.  Raw String to ignore escape sequence 
#           Sometimes we may wish to ignore the escape sequence inside a string. To do this we can place "r" or "R" infront of string.
#           This will imply that is a raw string and any escape sequence inside it will ignore.

# Don't use 'r' or 'R'
print("This is \x61 \ngood example")

# using 'r' or 'R'
print(r"This is \x64 \ngood example")
print(R"You are \x73 \n a peak at High school")



#-------------------------------------------------------------------------------------------------------------------------------------------#

#   3.  The "format()" Method for Formatting Strings
#           The "format()" method that is available with the string object is very versatile and powerful in formming string. format strings 
#           contains curly braces {} as placeholders or raplacement fields which gets replaced.

# We can use positional arguments or keyword arguments to specify the order.

#default (implicit) order
defaultOrder = "{}, {} and {}".format('Ali', 'Bella', 'Faness')
print('\n ------Default Order -------')
print(defaultOrder)

#order using positional argument
positionalOrder = "{1}, {0} and {2}".format("Ali", "Bella", "Faness")
print("\n ------ Positional order ------ ")
print(positionalOrder)

#order using keyword argument
keywordOrder = "{f}, {a}, {b}".format(f = "Faness", a = "Ali", b = "Bella")
print("\n ----- Keyword order ------")
print(keywordOrder)


# The "format()" method can have optional format specifications. They are separated from field name using colon. For example, we can left-justify
# "<", right justify ">" or center "^" as string in the given space. We can also format integers as binaty, hexadecimal ect. And float can be 
# rounded or displayed in the exponent format. There are a ton of formtting you can use.

#formatting integers
print("Binary repensentation of {0} is {0:b}".format(12))

#formatting floats
print("Exponent representation: {0:e}".format(1780.472))

#formatting alignment
print("|{:<10}|{:^10}|{:>10}|".format("Tiger", "Loin", "Panter"))


#----------------------------------------------------------------------------------------------------------------------------------------------#

#   4.  Old style formatting
#       We can even formate string like the old "sprintf()" style used in C programming language. We use the "%" operator to accomplish this

num = 3.14134314134
print("The value of num is %3.2f " %num)
print("The value of num is %3.5f " %num)


#---------------------------------------------------------------------------------------------------------------------------------------------#

#   5.  Common Python String Methods
#           There are numerous methods available with the string object. The "format()" method that we mentional above is one of them.
#           Some of the commonly used methods are "lower()", "upper()", "join()", "split(), "find()", "replace()", etc. 

# using "lower()"
print("Google For ExtenDED".lower())

# using "upper()"
print("google for people".upper())

# using "split()"
print("This will split all worl into a list:".split())

# using "join()"
print("google to".join(["search", "specifict", "things"]))

#using "replace()"
print("Happle Monday dued!!".replace("dued!!", "Man!!"))




# at the end of basic python strings
