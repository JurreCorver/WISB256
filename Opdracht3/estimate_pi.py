import random
import math
import sys

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print("Use: python estimte_pi.py N L")
    exit()
#elif float(sys.argv[2]) > 1:
#    print("AssertionError: L should be smaller than 1")
#    exit()
else:
    N = int(sys.argv[1]) #aantal keer herhalen experiment
    L = float(sys.argv[2])  #lengte naald
    
    if len(sys.argv) == 4:
        seed = int(sys.argv[3])
        random.seed(seed)


def drop_needle(L):
    # uniform in [0,1]
    x0 = random.random()
    # uniform in [0,2\pi]
    a = random.vonmisesvariate(0,0)
    
    xeind = x0 + L * math.cos(a)
    if xeind < 0 or xeind > 1:
        return True
    else:
        return False
        
count = 0    
for i in range(0, N):    
    if drop_needle(L):
        count += 1


p = count/N
    
if L < 1:
    pi = (2*L)/p
else:
    #pi = (2 * L)/(p-1) - (2/(p-1))*(math.sqrt(L**2 -1) + 1/math.sin((1/L)))
    pi = (2 * L)/(p-1) - (2/(p-1))*(math.sqrt(L**2 -1) + math.asin((1/L)))

print(count, "hits in" , N, "tries" ) 
print("Pi =", pi)

