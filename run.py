def get_user_input():
    """
    gets user input to choose between 3 menu options
    """
    user_input = input("enter desired options here: ")

    try:
        return input_validation(user_input)
    except ValueError as error:
        print(f"Invalid input: {error}, please try again.")
        get_user_input()


def input_validation(user_input):
    """
    This function validates whether the user input is an integer or not
    """
    valid_options = [1,2,3]
    parsed = int(user_input)
    if parsed not in valid_options:
        raise ValueError(
            f"Needs to be an value between 1, 2 or 3 you provided {user_input}"
        )
    
    return parsed

def start_game():
    print('game started')

def intructions():
    print("some istructures")

def credits():
    print('made by patrick')

def main():
    print("Please enter the input of the desired option")
    print("The input needs to be a number between 1 and 3 \n")
    print("1.start Game")
    print("2.Instructions")
    print("3.Credits\n")
    user_input = get_user_input()
    if user_input == 1:
        return start_game()
    if user_input == 2:
        return intructions()
    if user_input == 3:
        return credits()
main()