34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. Go to the editor


x = int(input(" Please Enter the First Value a: "))
y = int(input(" Please Enter the Second Value b: "))
c=x+y
if c>=15 and c<=20:
    print("The sum is 20")
else:
    print(c)
    
