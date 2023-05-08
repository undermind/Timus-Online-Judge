import sys
#s = sys.stdin.read()
theS=""
#for c in s:if c in ['(',')','[',']']:theS+=c 
#theS= "([(]"
theS="([][]())"
memo = [[-1 for i in range(100)] for j in range(100)]
l = len(theS)
def solve(s,e):
    if s>e: return 0
    if memo[s][e]==-1:
        memo[s][e]=1+solve(s+1,e)
        if (theS[s] in ['(','[']):
            for i in range(s+1,e+1):
                if (theS[s]=='(' and theS[i]==')') or (theS[s]=='[' and theS[i]==']'):
                    memo[s][e] = min(memo[s][e],solve(s+1,i-1)+solve(i+1,e))
    return memo[s][e]

def sprn(s,e):
    if (s>e): return
    best = solve(s,e)
    if (1+solve(s+1,e)==best):
        if theS[s]=='(' or theS[s]==')':print("()",end="")
        else: print("[]",end="")
        sprn(s+1,e)
        return
    for i in range (s+1,e+1):
        if ((theS[s]=='(') and (theS[i]==')'))or ((theS[s]=='[') and (theS[i]==']')):
            if theS[s]=='(': 
                print("(",end="")
                sprn(s+1,i-1)
                print(")",end="")
                sprn(i+1,e)
            else:
                print("[",end="")
                sprn(s+1,i-1)
                print("]",end="")
                sprn(i+1,e)
            return



sprn(0,l-1)