"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# repeat forever:
while True: 
#     read input
    input_string = input("Enter your equation: ")

# strip whitespace off end of input
    input_string = input_string.rstrip()
    
#     tokenize input
    token = input_string.split(" ")
    
    x = token[0]
 
#         if the first token is "q":
#             quit
    if x == "q":
        print("Thanks for playing math!")
        quit() 

#        (decide which math function to call based on first token)
#             if the first token is 'pow':
                #if x == "pow"
#                   call the power function with the other two tokens

#             (...etc.) 

    elif len(token) < 2:
        print("Please enter at least 2 characters.")
        
    elif len(token) >= 2:
        y = int(token[1])
        

        if len(token) == 2:
       
            if x == "square":
                print(square(y))
                continue
            elif x == "cube":
                print(cube(y))
                continue
        
        elif len(token) == 3:
            z = int(token[2]) 
            
            if x == "+":
                print(add(y, z))
                continue
            elif x == "-":
                print(subtract(y, z))
                continue
            elif x == "*":
                print(multiply(y, z))
                continue
            elif x == "/":
                print(divide(y,z))
                continue
            elif x == "mod":
                print(mod(y, z))
                continue
            elif x == "pow":
                print(power(y, z))
                continue
