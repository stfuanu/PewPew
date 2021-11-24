# Enter your code here. Read input from STDIN. Print output to STDOUT
# 1 4
# x**3 + x**2 + x + 1


x , k = input().split(" ")

ans = eval(input().replace("x",x))
# print(ans)

# eval function parses the expression argument and evaluates it as a python expression

# syntax : eval(expression, [globals[, locals]])

# eval("print('AnAnAlAu'.replace('A','Z'))")
# eval("print('AnAnAlAu'.replace('A','Z'))")
# eval("print('AnAnAlAu'.replace('A','Z',0))")
# eval("print('AnAnAlAu'.replace('A','Z',-1))")

if ans == int(k) :
    print("True")
else:
    print("False")
    
