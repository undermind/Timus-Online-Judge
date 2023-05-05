import sys

#tokens = sys.stdin.read().split()
tokens = ['3','5','7','5']
K= int(tokens[0])
groups=[0]*K
for i in range(K):
    groups[i]=int(tokens[i+1])
#print(groups)
groups.sort()
cnt=0
for i in range((K//2)+1):
    cnt+=(groups[i]//2)+1
print(cnt)