110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function. Go to the editor

num_list = [45, 55, 60, 37, 100, 105, 220]
i=0
while i<len(num_list):
    if num_list[i]%15==0:
        print(num_list[i])
    i=i+1
