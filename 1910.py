import sys
tokens = sys.stdin.read().split()
#tokens=[6,1, 4, 4, 4, 1, 1]
#tokens=[3,1,2,3]
n=int(tokens[0])
maxsum=0
maxn=-1
t=[0]*n
for i in range(n):
    t[i]=int(tokens[i+1])
#print(t)
for i in range(1,n-1):
    if t[i-1]+t[i]+t[i+1]>maxsum:
        maxn=i+1
        maxsum=t[i-1]+t[i]+t[i+1]

print(maxsum,maxn)
