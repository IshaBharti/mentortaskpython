5. Write a Python function to calculate the factorial of a numbe


def fact(user):
    i=1
    fact=1
    while i<=(user):
        fact=fact*i
        i=i+1
    return fact
a=int(input("enter a numver"))
print(fact((a)))
                                                                  
