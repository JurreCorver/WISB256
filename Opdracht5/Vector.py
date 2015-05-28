__AUTHOR__  = 'Jurre'
from array import array

class Vector():
    
    __slots__ = ('_n', '_vect')
    
    def __init__(self, n = 3, vect = 0):
        self._n = n
        self._vect = vect
        
        
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
    
    def clone(self):
        return Vector(self._n, [self._vect[i] for i in range(0, self._n)])
        
        
def GrammSchmidt(V):
        
    
    n = len(V)
    vectlist = [V[i] for i in range(0,n)]
    
    for i in range(0, n):
        for j in range(0, i):
            vectlist[i] = Vector.lincomb(vectlist[i],  proj(V[i], vectlist[j] ) ,1, -1)
            
    for i in range(0,n):
        grootte = (1/vectlist[i].norm())
        vectlist[i] = vectlist[i].scalar(grootte)
    
    return vectlist        
    
        
   # for i in range(0,n):
    #    for j in range(0, i):
     #       V[i] = V[i].lincomb(proj(vectlist[j]), 1, -1)
      #  #print V[i]
       # vectlist.append(V[i])
    #return vectlist
        
def proj(q, r):
    
    
    vect = r.scalar(q.inner(r)/(r.inner(r)))
    return(vect)    