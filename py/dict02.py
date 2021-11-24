n = int(input())
# wo = []
# for x in range(n) :
#     wo.append(input())
# # print(wo)
# print(len(set(wo)))
occ = {}

for x in range(0,n) :
    strr = input()
    if strr in occ.keys():
        occ[strr] = occ.get(strr,0) + 1
    else :
        occ[strr] = 0

print(len(occ.keys()))
print(" ".join( str(x) for x in list(occ.values())))
