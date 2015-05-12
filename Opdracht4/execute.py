import bisection
import math

def f(x):
    return(x*x)

root = bisection.findRoot(f,0,3,.0000000000001)

print(root)