import sys
tokens = sys.stdin.read().split()
n=int(tokens[0])

cnt = {
"Emperor":0,
"Macaroni":0,
"Little":0,
"Penguin":0
}
for i in range(n*2):
    cnt[tokens[i+1]]+=1

if cnt["Emperor"]>cnt["Little"] and cnt["Emperor"]>cnt["Macaroni"]: print("Emperor Penguin")
elif cnt["Little"]>cnt["Macaroni"]: print("Little Penguin")
else: print("Macaroni Penguin")