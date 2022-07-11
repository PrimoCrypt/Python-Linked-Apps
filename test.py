
from calendar import c


one = "1. Calculator"
two = "2. Hello your name"
programList = [one , two]

error = print("this is an error")
def appList(programList):
    for dispList in programList:
        return dispList
appList
selection = input(f"pick from these list{appList(programList)}: ")
if (selection == "1"):
    def calculator(selection):    
        x = int(input("x: "))
        sign = input("sign(* , + , - or /): ")
        y = int(input("y: "))

        if (sign == "+"):
            print(f"result for {x} + {y} = {x + y}")
        elif (sign == "-"):
            print(f"result for {x} - {y} = {x - y}")
        elif (sign == "*"):
            print(f"result for {x} x {y} = {x * y}")
        elif (sign == "*"):
            print(f"result for {x} / {y} = {x / y}")
        else:
            print("Unrecognized input, please try again later")
    calculator
