import random

def play():

    board_list = ['0','1','2','3','4','5','6','7','8']

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


    your_sign = input("\nWhat symbol do you want to play with? Choose O or X")
    opponent_sign = str
    while your_sign not in ['o', 'O', 'x', 'X']:
        your_sign = input("Please choose valid symbol. Choose O or X")

    else:
        if your_sign == 'o' or your_sign == 'O':
            opponent_sign = 'X'

        else:
            opponent_sign = 'O'


    def keep_playing():
        yes_no = input("Do you want to keep playing? If so press y, if no choose n")
        while yes_no == 'y':
            print('Ok, lets play')



            play()
        else:
            try:
                while yes_no == 'n':
                    print('Nice game! See you next time')

                    break
            except yes_no not in ['n']:

                raise ValueError
                yes_no = input("Wrong value, If yes press y, if no choose n")


    def game_on():

        free_indexes_tracker = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        while len(free_indexes_tracker) > 0:

            position_index = int(input("Please choose the position you want to place your symbol"))
            while position_index not in free_indexes_tracker:
                position_index = int(input("Please choose a valid number from the list {}".format(free_indexes_tracker)))
            else:
                board_list[position_index] = your_sign
                free_indexes_tracker.pop(free_indexes_tracker.index(position_index))  # removing position from the list
                random_position_from_tracker = random.choice(free_indexes_tracker)  # picking a random position for opponent
                board_list[random_position_from_tracker] = opponent_sign
                free_indexes_tracker.pop(free_indexes_tracker.index(random_position_from_tracker))
                print_board(board_list)

                if len(free_indexes_tracker) <= 4:
                    def win():
                        if board_list[0] == board_list[1] == board_list[2]:
                            return " Person playing with {} won!".format(board_list[0])

                        elif board_list[3] == board_list[4] == board_list[5]:
                            return " Person playing with {} won!".format(board_list[4])

                        elif board_list[7] == board_list[8] == board_list[6]:
                            return " Person playing with {} won!".format(board_list[6])

                        elif board_list[0] == board_list[3] == board_list[6]:
                            return " Person playing with {} won!".format(board_list[0])

                        elif board_list[1] == board_list[4] == board_list[7]:
                            return " Person playing with {} won!".format(board_list[1])

                        elif board_list[2] == board_list[5] == board_list[8]:
                            return " Person playing with {} won!".format(board_list[5])

                        else:
                            while False:
                                continue
                    print(win())
                    if win():
                        keep_playing()

    print_board(board_list)
    game_on()

play()






