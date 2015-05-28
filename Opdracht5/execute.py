from Vector import *

from array import array

#bestaat het double type? kunnen we checken of iets double is?

p = Vector(3, [1, 1.00, 1.000])
q = Vector(3, [1,2,3])

v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])

W = GrammSchmidt([v0,v1])


print(W[1])
print(W[0].inner(W[1]))
print(W[0].norm())