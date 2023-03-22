"""
A simple TIC TAC TOE inspired game for two players.
"""
import random

"""
 Function changing string to red
"""


def p_red(obj):
    return "\033[91m{}\033[00m".format(obj)


"""
# Function changing string colour to green
"""


def p_green(obj):
    return "\033[92m{}\033[00m".format(obj)


print('\n'*48)  # Clearing the screen

"""
Main function of the game.
"""


def play():
    board_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    def print_board(board):

        print(' --- --- ---')
        print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2]+ ' | ')
        print(' --- --- ---')
        print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5]+ ' | ')
        print(' --- --- ---')
        print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8]+ ' | ')
        print(' --- --- ---')
        return board

    print_board(board_list)

    your_sign = input("\nWhat symbol do you want to play with? Choose o or x")
    opponent_sign = str

    while your_sign not in ['o', 'x']:
        your_sign = input("Please choose valid symbol. Choose o or x")
    else:
        if your_sign == 'o':
            opponent_sign = 'x'
        else:
            opponent_sign = 'o'

    def keep_playing():

        yes_no = input("Do you want to keep playing? If so press y,"
                       " if no choose n")
        while yes_no == 'y':
            print('Ok, lets play')
            print('\n'*20)
            play()
        else:
            while yes_no != 'n':
                yes_no = input("Please choose y if you want to keep "
                               "playing or no if you want to quit.")
                continue
            else:
                print('Nice game! See you next time')
                quit()

    def win():

        if board_list[0] == board_list[1] == board_list[2]:
            return f" Person playing with {board_list[0]} won!"

        if board_list[3] == board_list[4] == board_list[5]:
            return f" Person playing with {board_list[4]} won!"

        if board_list[7] == board_list[8] == board_list[6]:
            return f" Person playing with {board_list[6]} won!"

        if board_list[0] == board_list[3] == board_list[6]:
            return f" Person playing with {board_list[0]} won!"

        if board_list[1] == board_list[4] == board_list[7]:
            return f" Person playing with {format(board_list[1])} won!"

        if board_list[2] == board_list[5] == board_list[8]:
            return f" Person playing with {board_list[5]} won!"
        if board_list[0] == board_list[4] == board_list[8]:
            return f" Person playing with {board_list[4]} won!"
        if board_list[2] == board_list[6] == board_list[4]:
            return f" Person playing with {board_list[4]} won!"
        else:
            while False:
                continue

    def game_on():

        free_indexes_tracker = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        while len(free_indexes_tracker) >= 0:

            position_index = int(input("Please choose the position "
                                       "you want to place your symbol"))
            while position_index not in free_indexes_tracker:
                position_index = int(input(f"Please choose a valid number"
                                           f" from the list {free_indexes_tracker}"))
            else:
                board_list[position_index] = p_green(your_sign)
                free_indexes_tracker.pop(free_indexes_tracker.index(position_index))  # removing position
                # from the list
                random_position_from_tracker = random.choice(free_indexes_tracker)  # picking a random position
                # for opponent
                board_list[random_position_from_tracker] = p_red(opponent_sign)
                free_indexes_tracker.pop(free_indexes_tracker.index(random_position_from_tracker))
                print('\n'*100)
                print_board(board_list)

                if len(free_indexes_tracker) <= 4:

                    print(win())
                    if win():
                        keep_playing()

                if len(free_indexes_tracker) == 0 and not win():
                    print("It is a draw, try your luck next time!")
                    keep_playing()

    print_board(board_list)
    game_on()


play()
