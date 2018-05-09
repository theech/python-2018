#Python Set Operations
#   sets can be use to carry out mathematical set operations like union, intersection, difference and symmetric difference. we can do this with
#   Operators or methods. 

#   1.  Set Union
#           Union of A and B is a set of all elements from both sets. Union is performed using "|" operator. Same can be using method "union()"


#initialize set A and set B

A = {1, 2, 3, 4, 7}
B = {3, 4, 5, 6, 7, 8, 9}
print(A)
print(B)

#using "|" operator (A or B)
C = A|B
print(C)

#or you can use "union()"
D = A.union(B)
E = B.union(A)
print(D)
print(E)

#                   A|B = B|A 
#                   A.unoin(B) = B.union(A)


#-----------------------------------------------------------------------------------------------------------------------------------------------#
#   2.  Set intersection
#           Intersection of A and B is a set of Elements that common in both sets. Intersection is performed using "&" operator. Same can be
#           using the method "intersection()".

#using "&"
C = A&B
print(C)

#using "intersection()"
C = A.intersection(B)
print(C)

#                   A & B = B & A
#                   A.intersection(B) = B.intersection(A)

#----------------------------------------------------------------------------------------------------------------------------------------------#
#   3.  Set Difference 
#           Difference of A and B (A - B) is a set elements that are only in A but not in B. Similarly, B - A is set of element in B. But not in A
#           Difference is performed using "-" operator. Same can be accomplished using the method "difference()"

#using "-"
C = A - B
D = B - A

print(C)
print(D)

#using "difference()"
C = A.difference(B)
D = B.difference(A)

print(C)
print(D)

#                   A - B != B - A
#                   A.difference(B) != B.difference(A)

#-------------------------------------------------------------------------------------------------------------------------------------------#
#   4.  Set Symmetric Difference
#           Symmetric Difference of A and B is a set of elements in both A snd B except those that are common in both.
#           Symmetric difference is performed using "^" operator. Same can be accomplished using the method "symmtric_difference()"

#using "^"
C = A ^ B
D = B ^ A

print(C)
print(D)

#using "symmetric_difference()"
C = A.symmetric_difference(B)
D = B.symmetric_difference(A)

print(C)
print(D)

#                   A ^ B = B ^ A
#                   A.symmetric_difference(B) = B.symmetric_difference(A)

#-------------------------------------------------------------------------------------------------------------------------------------------#
#   5.  Set Membership Test
#           we can test if an item exists in a set or not, using the keyword "in"

#initialize set00
set00 = set("Apple Ipod Shuffle")
checkMember = 'I' in set00
print(checkMember)
print('z' not in set00)


#-------------------------------------------------------------------------------------------------------------------------------------------#

#copy set by using "copy()" method
set01 = {1,2,3,4,5,99}
set02 = set01.copy()
print(set02)



