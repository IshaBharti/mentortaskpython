Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERR



Age=int(input("enter yoy Age"))
employee=input("enter M/F")
marital=input("enter your marital  status=Y/N")
if employee=="F":
    print("she works on Urban Area")
elif employee=="M" or age>=20 and age<=40:
    print( "he works anywhere")
elif employee=="M" or age>=40 and age<=60:
    print(" He works on urban areas only")
else:
    print("Pagl mt bn")
