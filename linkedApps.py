
from calendar import c

one = "1. Calculator"
two = "2. Hello your name"
programList = [one , two]
selectionError = "this is an error with your selection"

print("pick from these list")
print("")
print("    1. Calculator")
print("    2. Hello Your Name")
print("")

selection = int(input(f"enter your option: "))
if (selection == 1):
    print("")
    print("Calculator Loading...")
    print("")
    print("Welcome to Calculator app")
    print("")
    from calculator import calculator
elif (selection == 2):
    print("")
    print("Hello Loading...")
    print("")
    print("Welcome to Hello your name app")
    print("")
    from hello import hello
else:
    print(selectionError)
    print(f"Input not available pick either {one} or {two}")
