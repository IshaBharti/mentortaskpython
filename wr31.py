Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each othe


def check(data):
    if len(data)==len(set(data)):
        return"True"
    else:
        return"false";
print(check([2,4,5,7,9]))
