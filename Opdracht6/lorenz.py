__AUTHOR__  = 'Jurre'
from array import array
import numpy as np
from scipy.integrate import odeint
from numpy.linalg import eig

class Lorenz():
    
    __slots__ = ('_sigma', '_rho', '_beta', '_xyz', '_sol', '_sol2')
    
    def __init__(self, xyz, sigma = 10, rho = 28, beta = 8/3.0):
        self._sigma = sigma
        self._rho = rho
        self._beta = beta
        self._xyz = xyz
        self._sol = 0
        self._sol2 = []
        
        
        
       
    def __str__(self):
        
           
        return(str(self._sol))
    
    #def __getitem__(self, a, b):
        #return self._sol
    
    def df(self, u):
            deriv = np.array([[-self._sigma, self._sigma, 0], [self._rho - u[2], -1, -u[0] ], [u[1], u[0], -self._beta]])
            return(deriv)
    
    def isStable(self,u):
        eigens = eig(self.df(u))[0].real
        #print(eigens)
        
        for i in eigens:
            if i >= 0:
                return False
        
        return True       
        
        

    def solve(self, T,dt):
        
        def f(y, t):
         
            
            f0 = self._sigma * (y[1] - y[0])
            f1 = y[0] * (self._rho - y[2]) - y[1]
            f2 = y[0]*y[1] - self._beta * y[2]
            
            return [f0, f1, f2]

        # initial conditions
        y0 = self._xyz
        #t  = np.linspace(0, T, T/dt+1)# time grid
        t = np.arange(0, T, dt)
        
        #print(t[0::10])
        #print(t[-1])
        
        # solve the DEs
        soln = odeint(f, y0, t)
        S = soln[:, 0]
        #Z = soln[:, 1]
        #R = soln[:, 2]
        self._sol = S
         
        return soln
            

 