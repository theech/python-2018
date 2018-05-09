#Python Set Operations
#   sets can be use to carry out mathematical set operations like union, intersection, difference and symmetric difference. we can do this with
#   Operators or methods. 

#   1.  Set Union
#           Union of A and B is a set of all elements from both sets. Union is performed using "|" operator. Same can be using method "union()"


#initialize set A and set B

A = {1, 2, 3, 4, 7}
B = {3, 4, 5, 6, 7, 8, 9}

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

