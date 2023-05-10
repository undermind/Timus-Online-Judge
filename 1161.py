#1161
import sys,math
#tokens = sys.stdin.read().split()
tokens = [3,72,30,50]
n=int(tokens[0])
w=[]
for i in range(n):
    w.append(int(tokens[i+1]))
#w.sort(reverse=True)
w.sort()
while len(w)>1:
    w.append(2*math.sqrt(w.pop()*w.pop()))

print("%.2f" % w[0])
#print(w)
