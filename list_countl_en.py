Exercise Question 6: Given a number count the total number of digits in a number



a= 10, 20,30, 40, 50
print(len(a))
 #or 
count=0
number = int(input("Enter a number "))
while (number > 0):
  number = number//10
  count = count + 1
print ("Total number of digits : ",count)

