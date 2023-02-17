import sys
#print (tokens)
telcode = ["oqz","ij","abc","def","gh","kl","mn","prs","tuv","wxy"]
        
def wordhash(wrd):
    res=""
    for ch in wrd:
        for digit in range(10):
            if ch in telcode[digit]:
                res=res+str(digit)
    return res

def checkwordfits(pos):
    #global thedict
    #global num
    fitwords=[]
    for w in thedict:
        #word not fits by size
        if len(w)+pos>len(num): continue
        wordfits=True
        for i in range(len(w)):
            if (thedict[w][i]!=num[pos+i]):
                wordfits=False
                break
        if wordfits:
            fitwords.append(w)
    return fitwords



tokens = sys.stdin.read().split()
# tokens = ['7325189087', '5', 'it', 'your', 'reality', 'real', 'our', '4294967296', '5', 'it', 'your', 'reality', 'real', 'our', 
# '2222223222222222322222222222322222222232222222222232222222223222222222223222222222322222',
# '5',
# 'a',
# 'aa',
# 'afa',
# 'aaaa',
# 'aafaa',
# '-1']
i=0
while True:
    num=tokens[i]
    if (num=="-1"): break
    i+=1
    size=int(tokens[i])
    i+=1
    dct=tokens[i:i+size]
    thedict= {w:wordhash(w) for w in dct}
#    print (num,"=>",thedict)
    solutions=[[]*0]*(len(num)+1)
    for it in range(len(num)):
        fw=checkwordfits(it)
        for w in fw:
            if (i+len(w))<=len(num):
              if (len(solutions[it+len(w)])==0)or(len(solutions[it]+[w])<(len(solutions[it+len(w)]))):
                if it==0:
                    solutions[it+len(w)]=[w]
                else:
                    if (len(solutions[it])):
                      solutions[it+len(w)]=solutions[it]+[w]
        #print(it,num[it],fw)

#    print(solutions[-1])
    if len(solutions[-1]):
        solo=solutions[-1]

        for it in range(len(solo)):
            if it<len(solo)-1:
                print(solo[it],"",end='')
            else:
                print(solo[it])
    else:
        print("No solution.")


    i+=size
