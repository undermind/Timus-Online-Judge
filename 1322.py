import sys
#print (tokens)


tokens = sys.stdin.read().split()
#tokens = ['3', 'rdarcaaaabb']
n=int(tokens[0])-1
word=tokens[1]
inv={}
for i in range(len(word)):
    inv[i]=word[i]
inv = sorted(inv.items(), key=lambda x:x[1])
for i in range(len(word)):
    n=inv[n][0]
    print(word[n],end='')

