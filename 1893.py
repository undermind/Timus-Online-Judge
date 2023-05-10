import sys
place = sys.stdin.read().split()
sym=place[0][-1]
num=int(place[0][:-1])
#print(num,sym)
# 1-2
#A BC D
#A BC D
# 3-20
# AB CD EF
# 21-65
#ABC DEFG HJK
if num <3:
    if sym in ['A','D']:print("window")
    else: print("aisle")
elif num<21:
    if sym in ['A','F']:print("window")
    else: print("aisle")
else:
    if sym in ['A','K']:print("window")
    elif sym in ['C','D','G','H']:print("aisle")
    else: print("neither")
