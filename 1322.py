import sys
#print (tokens)

#tokens = sys.stdin.read().split()
tokens = ['3', 'rdarcaaaabb']
n=int(tokens[0])-1
word=tokens[1]
l=len(word)
inv=[0]*l
for i in range(l):
    inv[i]=(ord(word[i])<<16) + i

inv = sorted(inv)

for i in range(len(word)):
    n=inv[n]%(65536)
    print(word[n],end='')
