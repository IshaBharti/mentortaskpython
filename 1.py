7. Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]
b=[]
i=0
while i <len(a):
    if a[i] not in b:
        b.append(a[i])
    
    i=i+1
print(b)
