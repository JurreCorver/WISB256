#Sieve_of_E.py - second hand-in

import time
import math
import sys


T1 = time.perf_counter()
N = int(sys.argv[1])
file = str(sys.argv[2])
primestate = []
for r in range(0, N):
    primestate.append(True)
primestate[0] = False
primestate[1] = False

for i in range(2, int(N**0.5 + 1) ):
    if primestate[i]:
        for j in range(i**2, N, i):
            primestate[j] = False

primedata = open(file, 'w')
amount = 0
for i in range(2, N):
    if primestate[i]:
        primedata.write(str(i)+'\n')
        amount+=1

        

T2 = time.perf_counter()
print('Found' ,amount, 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.\n --------------------------------------------')  
