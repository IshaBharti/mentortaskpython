14. Write a Python program to calculate number of days between two dates.


from datetime import date
a = date(2020, 2, 8)
a1 = date(2020, 5, 31)
diff = a1 - a
print(diff.days)
