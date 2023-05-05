import math

sol={}
sol[0]=0
y=0
for n in range(1,100000001):
    x= n
    a = ((y-1)*(x ** 5))
    b = (x ** 3) 
    c = -x*y 
    d = 3*x 
    e = 7*y 
    y=(a+b+c+d+e)% 9973
    #print(n, sol[n])
    if n % 10000 ==0: sol[n]=y


print(list(sol.values()))