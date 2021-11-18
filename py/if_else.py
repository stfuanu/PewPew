import random

n = random.randint(1,22)

# My Take :

if (n%2!=0):
    print("Weird")
elif (n%2==0):
    if n>=2 and n<=5 : # use range instead
        print("Not Weird")
    elif n>=6 and n<=20 : # combine multiple statements
        print("Weird")
    elif n>20 :
        print("Not Weird")
else :
    print("No Weird")


# Example :

if n in range(6,21) or n%2!=0:
    print("Weird")
else:
    print("Not Weird")


# Example :
check = {True: "Not Weird", False: "Weird"} #dictionary , kindof like maps in golang

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])


# Example :

print("Weird") if n%2!=0 else print("Not Weird") if n in range(2, 5) or n > 20 else print("Weird")

# Example :

print('Weird' if (n%2!=0 or (n>=6 and n<=20))else 'Not Weird')
print('Weird' if n%2==1 or 6<=n<=20 else 'Not Weird') # maybe don't even need brackets