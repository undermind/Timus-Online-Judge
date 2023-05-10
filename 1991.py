import sys
tokens = sys.stdin.read().split()
#tokens=[4, 5,2, 7, 5, 0]
n=int(tokens[0])
k=int(tokens[1])
bumbum=[0]*n
droids=0
bbleft=0
for i in range(n):
    bumbum[i]=int(tokens[i+2])
    war=k-bumbum[i]
    if war>0:droids+=war
    else: bbleft-=war
print(bbleft,droids)
