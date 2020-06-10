var_x=int(input("enter number"))
var_y=int(input("enter a number"))
symbol=input("enter a symbol")
if symbol=="*":
    print("output is a",var_x*var_y)
if symbol=="%":
    print("output is a ",var_x%var_y)
if symbol=="+":
    print("output is a",var_x+var_y)
if symbol=="-":
    print("output is a",var_x-var_y)
if symbol=="":
    print("output is a",var_x/var_y)

