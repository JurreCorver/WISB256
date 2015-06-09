from lorenz import *
import numpy
from scipy.integrate import odeint

sigma = 10
rho = 0.9
beta = 8/3
L1 = Lorenz([-1,1,0],sigma,rho,beta)
u1 = L1.solve(50,.01)
L2 = Lorenz([-1.001,1.001,.001],sigma,rho,beta)
u2 = L2.solve(50,.01)
print(u1[0,0],u2[0,0]) # print values of x at t=0

print(u1[5000-1,0],u2[-1,0]) # print values of x at t=50

print(L1.df([1,1,1]))
print(L1.isStable([0,0,0]))


