# X for ship position and hit 
# '' avalible space
# "*" miss ship


from random import randint

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
    """
    Function that start game.
    """
    



player_board = [[' '] * 8 for x in range(8)]

computer_board = [[' ']* 8 for x in range(8)]

field_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'H': 4, 'L': 5, 'D': 6, 'H':7}




def call_board(board):
    """
    Function to call game board
    """
    print('  A B C D E F G H')
    print('  ---------------')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1

def call_ships(board):
    """
    Function to call game Ships
    """    
    for ship in range(5):
        ship_row = randint(0, 7)
        ship_column = randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row = randint(0, 7)
            ship_column = randint(0, 7)
        board[ship_row][ship_column] = 'X'  


def call_ships_location():
    """
    Function to call ships locations
    """
    row_check = [1,2,3,4,5,6,7,8]
    row = input('Please enter row from 1 - 8').upper()
    if row not in row_check:
        raise ValueError(
            f"Needs to be an value between 1-8 you provided {row}")    
        return row 

    

def call_ships_hits():
    """
    Function to call ships hits
    """
    pass

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