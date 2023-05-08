import sys
tokens = sys.stdin.read().split()
#tokens = ['5','5','8','13','27','14']
#tokens = ['5','5','5','4','3','3']
#tokens = ['4','15','16','30','2']
#tokens = ['1','1']
#tokens = ['3','2','2','2']
n=int(tokens[0])
w=[0]*n

sum=0

sums=[None]*1000000

for i in range(n):
    w[i]=int(tokens[i+1])
    sum+=w[i]
#w.sort()
#for i in range(n):
    if sums[w[i]]:
      sums[w[i]]=sums[w[i]]|{1<<i}
    else: sums[w[i]]={1<<i}

if n==1: 
   print(w[0])
   exit()

for i in range(sum+1):
  if sums[i]:
    for z in sums[i]:
      for j in range(n):
        if not ((1<<j) & z):
           y=i+w[j] #achive new sum
           if sums[y]: sums[y] =sums[y]|{z|(1<<j)}
           else:sums[y]={z|(1<<j)}


#for i in range(sum+1):if sums[i]:print(i,sums[i])

i=sum//2
while True:
  if sums[i] and sums[sum-i]: #есть сумма пополам
      if len(sums[i])+len(sums[sum-i])>1:
         for a in sums[i]:
            for b in sums[sum-i]:
               if (a & b ==0) and (a | b == (1<<n)-1):
                  print(sum-i*2)
                  exit()
  i-=1
#      print(i,len(sums[sum//2+i]))

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