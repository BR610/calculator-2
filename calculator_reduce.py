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

    if input_lst[0] == "+":
        return reduce(add, input_lst2)
    elif input_lst[0] == "-":
        return reduce(subtract,input_lst2)
    elif input_lst[0] == "*":
        return reduce(multiply, input_lst2)
    elif input_lst[0] == "/":
        return reduce(divide, input_lst2)
    elif input_lst[0] == "square":
        return square(input_lst2[0])
    elif input_lst[0] == "cube":
        return cube(input_lst2[0])
    elif input_lst[0] == "pow":
        return pow(input_lst2[0], input_lst2[1])
    elif input_lst[0] == "mod":
        return mod(input_lst2[0], input_lst2[1])


