__AUTHOR__  = 'Jurre'
from array import array

class Vector():
    
    __slots__ = ('_n, _vect')
    
    def __init__(self, n = 3, vect = 0):
        self._n = n
        
        
        if type(vect) is list:
            self._v = array('d', [vect[i] for i in range(0,n)])
        else:
            self._v = array('d', [vect for i in range(0,n)])
        
        
        
    def __str__(self):
        prt = ""
        for i in range(0,self._n - 1):
            prt += str(self._v[i]) + '\n'
        prt += str(self._v[self._n-1])    
           
        return(prt)
    
    def lincomb(self,other,alpha,beta):
        w = Vector(self._n, [alpha * self._v[i] + beta * other._v[i] for i in range(0, self._n) ])
        return w

    def scalar(self, alpha ):
        
        w = Vector(self._n, [alpha * self._v[i]  for i in range(0, self._n) ])
        return w
        
    def inner(self,other):
        w = 0 
        for i in range(0, self._n):
            w += self._v[i]* other._v[i]
        return w    
        
    def norm(self):
        w = 0
        for i in range(0, self._n):
            w += self._v[i]**2
        
        w = w**0.5
        
        return w