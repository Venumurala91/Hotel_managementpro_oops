def input_validity_check(message, start=0, end=None):
    inp = input(message).strip()
    

   
    if not inp.isdigit(): 
        print("Invalid input! You have chosen an invalid number.")
        return None

 
    inp_value = int(inp)

    if start is not None and end is not None:
        if not (start <= inp_value <= end):
            print(f"Invalid range! Please enter a number between {start} and {end}.")
            return None  
        else:
            return inp_value  

    else:
       
        return inp_value
