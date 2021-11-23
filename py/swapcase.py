# import string

inp = input()
print(inp.swapcase()) # //  using string method swapcase !


# my answer :
def swap_case(s):
    ss = list(s)
    newss = []
    for x in ss :
        if x.isupper() :
            newss.append(x.lower())
        elif x.islower() :
            newss.append(x.upper())
        else :
            newss.append(x)
    return "".join(newss)


# using list compri :

print("".join([i.lower() if i.isupper() else i.upper() for i in inp]) )
