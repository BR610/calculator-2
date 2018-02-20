def calculator_pre():
    """pre-fix calculator, takes in input and performs requested operations"""

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
    if input_lst[0] !in l2:
        return "Invalid entry"

    if input_lst[0] == "+" and len(input_lst2) == 2:
        return add(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "-" and len(input_lst2) == 2:
        return subtract(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "*" and len(input_lst2) == 2:
        return multiply(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "/" and len(input_lst2) == 2:
        return divide(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "square" and len(input_lst2) == 1:
        return square(input_lst2[0])
    elif input_lst[0] == "cube" and len(input_lst2) == 1:
        return cube(input_lst2[0])
    elif input_lst[0] == "pow" and len(input_lst2) == 2:
        return pow(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "mod" and len(input_lst2) == 2:
        return mod(input_lst2[0], input_lst2[1])
    else:
        return "Mismatched inputs"


