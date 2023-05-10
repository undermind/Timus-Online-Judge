import sys
tokens = sys.stdin.read().split()
a=int(tokens[0])
b=int(tokens[1])
if (a % 2==0)or(b%2==1):print("yes")
else: print("no")
