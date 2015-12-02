import random
import math
n=int(input())
Sum=0  
for v in range(0,n):
    h=5
    x=random.uniform(-5000,1)
    F = (-1/h*math.log(1-x))
    print('x=',x,'F=',F)
      
    Sum+=F
mw=Sum/n        
print('Sum=',Sum)
print('mat owidanie=',mw)    

    
    
    
    