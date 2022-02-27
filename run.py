def get_user_input():
    """
    gets user input to choose between 3 menu options
    """
    print("Please enter the input of the desired option")
    print("The input needs to be a number between 1 and 3 \n")

    user_input = input("enter desired options here: ")
    input_validation(user_input)

def input_validation(values):
    """
    This function validates whether the user input is an integer or not
    """
    try:
        [int(values)for value in values]
        if len(values) != 1:
            raise ValueError(
                f"Needs to be one value you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.")

get_user_input()    