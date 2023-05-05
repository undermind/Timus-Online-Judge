import sys
inp = int(sys.stdin.read())

sum = 0
if inp>0: 
    for i in range(1,inp+1):sum+=i
else:
    for i in range(1,inp-1,-1):sum+=i

print(sum)