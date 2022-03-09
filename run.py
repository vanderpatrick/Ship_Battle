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
    player_place_board = [[' '] * 8 for x in range(8)]
    computer__place_board = [[' '] * 8 for x in range(8)]

    letters_field = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    def print_board(board):
        print('  A B C D E F G H')
        print('  ---------------')
        row_number = 1
        for row in board:
            print('%d|%s|' % (row_number, '|'.join(row)))
            row_number += 1

    def create_ships(board):
        for ship in range(5):
            ship_row, ship_column = randint(0, 7), randint(0, 7)
            while board[ship_row][ship_column] == 'X':
                ship_row, ship_column = randint(0, 7), randint(0, 7)
            board[ship_row][ship_column] = 'X'

    def get_ship_location():
        row = input('please enter a ship row 1-8: ')
        while row not in '12345678':
            print('please enter valid row')
            row = input('please enter a ship row 1-8: ')
        column = input('please enter column from a - h').upper()
        while column not in 'ABCDEFGH':
            print('enter valid column')
            column = input('please enter column from a - h').upper()
        return int(row) - 1, letters_field[column]

    def count_hit_ships(board):
        count = 0
        for row in board:
            for column in row:
                if column == 'X':
                    count += 1
        return count

    create_ships(computer__place_board)
    turns = 3
    while turns > 0:
        print('welcome to battleship')
        print_board(player_place_board)
        row, column = get_ship_location()
        if player_place_board[row][column] == '-':
            print('you already guessed that')
        elif player_place_board[row][column] == 'X':
            print('congratulations u hit the shit')
            player_place_board[row][column] = 'X'
            turns -= 1
        else:
            print('missed')
            player_place_board[row][column] = '-'
            turns -= 1
        if count_hit_ships(player_place_board) == 5:
            print('sunk alles')
            break
        print(f'you have {turns} remaning')
        if turns == 0:
            print('gameOver')
            break


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
