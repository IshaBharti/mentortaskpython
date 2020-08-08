 Write a Python program to get the least common multiple (LCM) of two positive integers./




x = int(input(" Please Enter the First Value a: "))
y = int(input(" Please Enter the Second Value b: "))
if x>y:
    greater=x
    
else :
    greater=y
while (True):
    if(greater % x == 0 and greater % y == 0):
        lcm = greater
        break
    greater= greater + 1
    
print("\n Lcm of {0} and {1} = {2}".format(x, y, lcm))
