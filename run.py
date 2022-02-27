def get_user_input():
    """
    gets user input to choose between 3 menu options
    """
    print("Please enter the input of the desired option")
    print("The input needs to be a number between 1 and 3 \n")

    user_input = input("enter desired options here: ")
    
    try:
        input_validation(user_input)
    except ValueError as e:        
        print(f"Invalid input: {e}, please try again.")
        get_user_input()

valid_options = [1,2,3]

def input_validation(values):
    """
    This function validates whether the user input is an integer or not
    """
    
    if int(values) not in valid_options:
                
        raise ValueError(
            f"Needs to be an value between 1, 2 or 3 you provided {values}"
        )

get_user_input()