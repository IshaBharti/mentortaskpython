

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=0
n=0
t=0
x=0
u=0
g=0
while i< len(char_list):
    if char_list[i]=="a":
        a=a+1
    elif char_list[i]=="n":
        n=n+1
    elif char_list[i]=="t":
        t=t+1
    elif char_list[i]=="x":
        x=x+1
    elif char_list[i]=="u":
        u =u+1
    else:
        g=g+1
    i=i+1
print("a is =",a,"n is =",n,"t is =",t,"x is =",x,"u is =",u)
