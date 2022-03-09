from random import randint


def get_user_name():
    """
    Function to get username from player
    """
    player = input("Welcome to ShipBattle what is your name soldier ?: ")
    return player


def get_user_input():
    """
    gets user input to choose between 3 menu options
    """
    user_input = input("Enter desired options here: ")

    try:
        return input_validation(user_input)
    except ValueError as error:
        print(f"Invalid input: {error}, please try again.")
        get_user_input()


def input_validation(user_input):
    """
    This function validates whether the user input is an integer or not
    """
    valid_options = [1, 2, 3]
    parsed = int(user_input)
    if parsed not in valid_options:
        raise ValueError(
            f"provide value between 1, 2 or 3 you provided{user_input}")
    return parsed


def start_game():
    """
    Function that start game.
    """
    call_ships(computer_field)
    call_board(computer_field)
    call_board(player_field)
    call_ships(player_field)
    ship_size = [2, 3, 3, 4, 5]
    player_field = [[" "] * 8 for i in range(8)]
    computer_field = [[" "] * 8 for i in range(8)]
    player_guess = [[" "] * 8 for i in range(8)]
    computer_guess = [[" "] * 8 for i in range(8)]
    letters_translation = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def intructions():
    """
    Function that show user the instructions
    """
    print("some istructures")
    print("some istructures")
    print("some istructures\n")
    print("1.main menu")
    print("2.Start Game")
    user_input = get_user_input()
    if user_input == 1:
        return main()
    if user_input == 2:
        return start_game()


def credits_for_user():
    """
    function that shows user the credits
    """
    print('made by patrick\n')
    print('1.Main menu')
    print('2.Start Game')
    user_input = get_user_input()
    if user_input == 1:
        return main()
    if user_input == 2:
        return start_game()


def main():
    """
    function to call all functions
    """
    player = get_user_name()
    print(f"Please {player} enter the input of the desired option\n")
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
        return credits_for_user()


main()
