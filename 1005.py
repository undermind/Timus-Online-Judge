import sys
#tokens = sys.stdin.read().split()
tokens = ['5','5','8','13','27','14']
#tokens = ['5','5','5','4','3','3']
#tokens = ['4','15','16','30','2']
n=int(tokens[0])
w=[0]*n

sum=0

sums=[[]*0]*1000000

for i in range(n):
    w[i]=int(tokens[i+1])
    sum+=w[i]
    sums[w[i]]=[set(i)]



print(sums)


#for i in range(sum//2):
#  for el in sums[i]:
#    for j in range(n):
#      if not (j in el):
#        el.
#        sums[i+w[j]].append(el.)





#def dive(k1,k2,deep):
#    if deep==n:
#        #print(k1,k2)
#        return abs(k1-k2)
#    else:
#        return min(dive(k1+w[deep],k2,deep+1),dive(k1,k2+w[deep],deep+1))
#
#print(dive(0,0,0))

#w.sort(reverse=True)
#diff=0
#for i in range(n):
#    if diff>0:diff-=w[i]
#    else:diff+=w[i]
#print(abs(diff))