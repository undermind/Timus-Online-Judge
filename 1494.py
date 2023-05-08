import sys
tokens = sys.stdin.read().split()
#tokens=['2','2','1']
#tokens=['3','3','1','2']
#tokens=['4','3','1','4','2']
n=int(tokens[0])
max=-1
prev=0

a = []
for i in range(n):
    a.append(int(tokens[i+1]))

stack = []
max_taken = 0
for i in range(0, n):
    if a[i] > max_taken:
        for j in range(max_taken + 1, a[i] + 1):
            stack.append(j)

    last = stack[len(stack) - 1]
    if last == a[i]:
        if stack.pop() > max_taken:
            max_taken = last
    elif last > a[i]:
        print("Cheater")
        break
else:
    print("Not a proof")