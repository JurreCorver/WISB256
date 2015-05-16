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
solutions = []

def findAllRoots(f,a,b,epsilon):
    links = f(a)
    rechts = f(b)
    m = (a+b)/2
    midden = f(m)
    logarg = math.log(epsilon/ (b-a), 0.5)    
    intervalscount = math.ceil(logarg) #important
    intervals = 2**intervalscount
    interlen = (b-a)/intervals #important
    m_list = []
    if f(b) == 0:
        m_list.append(b)
        
    
    for i in range(0, int(intervals)):
        links = f(a+ i*interlen)
        rechts = f(a + (i+1)*interlen)
        m = (a+ i*interlen+a + (i+1)*interlen)/2
        midden = f(m)
        
        if links*rechts < 0:
            m_list.append(m)
        elif links == 0:
            m_list.append(a+ i*interlen)
            
        
    return(m_list)    