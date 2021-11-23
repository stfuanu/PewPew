# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
wo = []
for x in range(n) :
    wo.append(input())
# print(wo)
print(len(set(wo)))
occ = {}
i = 0
for x in wo :
    if x in wo[i:]:
        occ[x] = occ.get(x,0) + 1
    
    i += 1
print(" ".join( str(x) for x in list(occ.values())))
