# How to change or delete a string?
# String are immutable. This means that elements of a string cannot be changed once it has been assigned. We can simply reassing reassigns to the
#same name

string = "gunman"
#string[3] = 'B'

#If you uncomment line 6 you will get an error
#output : "typeError: 'str' object does not support item assignment"

#You can entire string
string = "Python"
print(string)

#output : "Python"


#--------------------------------------------------------------------------------------------------------------------------------------#
#We can not delete or remove character from a string. But deleting the String entirely is possible using the keyword "del".

#del string[1] 
#if you uncomment line 21 you will get an Error.
#"TypeError: 'str' object doesn't support item deletion"

#Delete entire string is possible 
del string

string # it will show you "NameError: name 'string' is not defined", because valiable "string" has been delete.






