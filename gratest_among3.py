
6.
Take input of age of 3 people by user and determine oldest and youngest among them.




a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
if a>=b and a>=c:
    print(a," first")
elif b>=a and b>=c:
    print(b,"first")
else:
    print(c,"first")

