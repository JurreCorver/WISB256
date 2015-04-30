import math
import sys

file = str(sys.argv[1])
primedata = open(file, 'r')
primelist = []

length = 0
twinlength = 0
while True:
    primelist.append(primedata.readline())
    
    
    if primelist[length] == '':
        del primelist[length ]
        break
    if length >= 1:
        if int(primelist[length]) == int(primelist[length-1]) +2:
            twinlength += 1
        
    
    length +=1    

N = float(primelist[length -1])   
numerator = length
denominator = N / math.log(N)
ratio = numerator/denominator 
C2 = 0.6601618
down = (2 * C2 * N)/ math.log(N)**2


print('Largest Prime = ' ,int( primelist[length-1]), '\n--------------------------------\n' + 'pi(N)         =  ' + str(length))  
print('N/log(N)      =  ' + str(denominator))
print('ratio         =  ' + str(ratio)+ '\n--------------------------------')
print('pi_2(N)       =  ' +str(twinlength) )
print('2CN/log(N)^2  =  ' + str(down))
print('ratio         =  ' + str(twinlength/down))
