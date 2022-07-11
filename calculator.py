def calculator():    
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
calculator()