import sys
tokens = sys.stdin.read().split()
n=int(tokens[0])
k=len(tokens[1])
answ=1
theN=n
if n%k==0:
    #N delitsya na K
   while n>=k:
      answ*=n
      n-=k
else:
   while n>=theN%k:
      answ*=n
      n-=k
  

print(answ)
