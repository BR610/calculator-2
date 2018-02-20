def calculator_pre():
    """pre-fix calculator, takes in input and performs requested operations"""

    from decimal import Decimal

    input_lst2 = []
    input_op = raw_input("Please enter your choice: ")
    input_lst = input_op.split(" ")
    
    if input_lst[0] == "q" or  input_lst[0] == "quit":
        return "Quitting function"
    else:
        try:
            for l in input_lst[1:]:
                l = float(l)
                input_lst2.append(l)
        except:
            return "Invalid  input"

    l2 = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
    if input_lst[0] not in l2:
        return "Invalid entry"

    if input_lst[0] == "+":
        return round(reduce(add, input_lst2), 2)
    elif input_lst[0] == "-":
        return round(reduce(subtract,input_lst2), 2)
    elif input_lst[0] == "*":
        return round(reduce(multiply, input_lst2), 2)
    elif input_lst[0] == "/":
        return round(reduce(divide, input_lst2), 2)
    elif input_lst[0] == "square":
        return round(square(input_lst2[0]), 2)
    elif input_lst[0] == "cube":
        return round(cube(input_lst2[0]), 2)
    elif input_lst[0] == "pow":
        return round(pow(input_lst2[0], input_lst2[1]), 2)
    elif input_lst[0] == "mod":
        return round(mod(input_lst2[0], input_lst2[1]),2)


