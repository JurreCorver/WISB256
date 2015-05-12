import math

def findRoot(f,a,b,epsilon):
    links = f(a)
    rechts = f(b)
    m = (a+b)/2
    midden = f(m)
    
    if abs(b-a) < epsilon:
        return(m)
        
    if links*midden <=0:
        sol = findRoot(f,a,m,epsilon) 
        return(sol)
        
    elif rechts*midden <= 0:   
        sol = findRoot(f,m,b,epsilon) 
        return(sol)