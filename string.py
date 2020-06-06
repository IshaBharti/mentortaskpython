list=[1,2,34,5,4,3,4,33]
list1=[8,6,5,4,3,42,2,5]
dup=[]
i=0
while i<len(list):
    j=0
    while j<len(list1):
        if list[i] in list1:
            dup.append(list[i])
        j=j+1
        i=i+1
print(dup)
a=0
b=[]
while a<len(dup):
    c=(dup[a]*dup[a])
    b.append(c)

    a=a+1
print(b)


    
