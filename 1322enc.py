order="ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"


#S=input("Input word>")
S="abracadabra"
S="a"
S="aaaaaaaaaaa"
S="Exactpro"
N=[S]
for i in range(1,len(S)):
    S=S[1:]+S[0]
#    print(i,S1)
    N.append(S)
S=S[1:]+S[0]
N.sort()
S1=""
answ=-1
for i in range(0,len(S)):
    if (N[i]==S)and(answ<0):
        answ=i+1
    S1+=N[i][-1]

print(answ)
print(S1)
