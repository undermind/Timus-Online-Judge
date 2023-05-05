order="ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"


#S=input("Input word>")
S="abracadabra"
S="a"
S="aaaaaaaaaaa"
N=[S]
for i in range(1,len(S)):
    S=S[1:]+S[0]
#    print(i,S1)
    N.append(S)
S=S[1:]+S[0]
N.sort()
S1=""
for i in range(0,len(S)):
    if N[i]==S:
        print(i+1)
    S1+=N[i][-1]


print(S1)
