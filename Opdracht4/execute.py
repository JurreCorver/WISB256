import bisection
import math

def f(x):
    return x**2

root = bisection.findRoot(f,-3,4.5 ,0.01)
print(root)

root2 = bisection.findAllRoots(f,-3,4,0.001)


print(root2)
#print(root)