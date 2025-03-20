
def input_validity_check(message,start=0,end=None):
    inp=input(message)

    if not inp.isdecimal:
        print("Invalid Input You have choosen")

    
    elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print("Invalid range. Try again!")
            else:
                return int(inp)

    else:
        return int(inp)
        
