3. Write a Python program to display the current date and time.
Sample Output :
Current date and time

import datetime
now = datetime.datetime.now()

print (now.strftime("%Y-%m-%d %H:%M:%S"))
