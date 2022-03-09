import random

import random


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
    ship_size = [2, 3, 3, 4, 5]
    player_field = [[" "] * 8 for i in range(8)]
    computer_field = [[" "] * 8 for i in range(8)]
    player_guess = [[" "] * 8 for i in range(8)]
    computer_guess = [[" "] * 8 for i in range(8)]
    letters_translation = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    def call_board(board):
        print('  A B C D E F G H')
        print('  ---------------')
        row_number = 1
        for row in board:
            print('%d|%s|' % (row_number, '|'.join(row)))
            row_number += 1

    def call_ships(board):
        for ships_length in ship_size:
            while True:
                if board == computer_field:
                    orientation = random.choice(['H', 'V'])
                    row = random.randint(0, 7)
                    column = random.randint(0, 7)
                    if check_ship_size(ships_length, row, column, orientation):
                        if check_overlap(board, row, column, orientation, ships_length) is False:
                            if orientation == "H":
                                for i in range(column, column + ships_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ships_length):
                                    board[i][column] = "X"
                            break
                else:
                    call_ships = True
                    print(f'Place the shipwith a length of {ships_length}')
                    row, column, orientation = player_call(call_ships)
                    if check_ship_size(ships_length, row, column, orientation):
                        if check_overlap(board, row, column, orientation, ships_length) is False:
                            if orientation == 'H':
                                for i in range(column, column + ships_length):
                                    board[row][i] = "X"
                            else:
                                for i in range(row, row + ships_length):
                                    board[i][column] = 'X'
                            call_board(player_field)
                            break

    def check_ship_size(ships_length, row, column, orientation):
        if orientation == "H":
            if column + ships_length > 8:
                return False
            else:
                return True
        else:
            if row + ships_length > 8:
                return False
            else:
                return True

    def check_overlap(board, row, column, orientation, ships_length):
        if orientation == 'H':
            for i in range(column, column + ships_length):
                if board[row][i] == "X":
                    return True
        else:
            for i in range(row, row + ships_length):
                if board[i][column] == "X":
                    return True
        return False

    def player_call(call_ships):
        if call_ships is True:
            while True:
                try:
                    orientation = input("enter orientation (H or V)").upper()
                    if orientation == "H" or orientation == "V":
                        break
                except TypeError:
                    print('enter a valid orientation H or V')
            while True:
                try:
                    row = input("enter the row 1-8 of the ship: ")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('enter a valid letter between 1-8')
            while True:
                try:
                    column = input('Enter the column of the ship: ').upper()
                    if column in 'ABCDEFGH':
                        column = letters_translation[column]
                        break
                except KeyError:
                    print('enter a valid letter between A_H')
            return row, column, orientation
        else:
            while True:
                try:
                    row = input("Enter the row 1-8 of the ship")
                    if row in '12345678':
                        row = int(row) - 1
                        break
                except ValueError:
                    print('enter a valid letter between 1-8')
            while True:
                try:
                    column = input('Enter the column of the ship: ').upper()
                    if column in 'ABCDEFGH':
                        column = letters_translation[column]
                        break
                except KeyError:
                    print('Enter a valid letter between A-H')
            return row, column

    def count_hits(board):
        count = 0
        for row in board:
            for column in row:
                if column == "X":
                    count += 1
        return count

    def turns(board):
        if board == player_guess:
            row, column = player_call(player_guess)
            if board[row][column] == '-':
                turns(board)
            elif board[row][column] == 'X':
                turns(board)
            elif computer_field[row][column] == "X":
                board[row][column] = 'X'
            else:
                board[row][column] = '-'
        else:
            row, column = random.randint(0, 7), random.randint(0, 7)
            if board[row][column] == "-":
                turns(board)
            elif board[row][column] == "X":
                turns(board)
            elif player_field[row][column] == "X":
                board[row][column] == "X"
            else:
                board[row][column] = "-"

    call_ships(computer_field)
    call_board(computer_field)
    call_board(player_field)
    call_ships(player_field)

    while True:
        while True:
            print('Guess a batlle ship location')
            call_board(player_guess)
            turns(player_guess)
            break
        if count_hits(player_guess) == 17:
            print("you win!")
            break

        while True:
            turns(computer_guess)
            break
        call_board(computer_guess)
        if count_hits(computer_guess) == 17:
            print('sorry you lost')
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
