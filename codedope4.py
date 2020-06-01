
4.
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.




salary=int(input("enter yor salary"))
year=int(input("enter a year"))
if year>5:
    print("congratulations  you got bonus",salary*5/100)
    
else:
    print("sorry you re not completed your 5 year ")
