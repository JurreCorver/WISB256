import bisection
import math

def f(x):
    return math.sin(x)

#root = bisection.findRoot(f,0,3,.0000000000001)

root2 = bisection.findAllRoots(f,1,9,0.001)


print(root2)
#print(root)