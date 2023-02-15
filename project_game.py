board_lines = []

line1 = [[0], [1], [2]]
line2 = [[3], [4], [5]]
line3 = [[6], [7], [8]]

board_lines = [line1, line2, line3]


def board():
    for line in board_lines:
        print(line)
    return board_lines


def tic_tac():
    board()


    def symbol_pick():
        player_one_symbol = input('Please choose o or x')

        while player_one_symbol not in ['o', 'x']:
            player_one_symbol = input('Please choose a valid symbol o or x')
        else:
            print("Thanks! You are going to play with {}".format(player_one_symbol))
            return player_one_symbol


    chosen_symbol = int
    chosen_symbol = symbol_pick()


    def game_on():

        position_index = input("Please choose the position you want to place your symbol")

        while position_index not in ['1', '2', '3', '4', '5', '6', '7', '8']:

            position_index = input("Please choose a valid number between 0 and 8")

        else:
            pos = int(position_index)

            if pos in [0, 1, 2]:
                line1[pos] = [chosen_symbol]
                """print( line1[position_index]) prints individual cell)"""
            elif pos in [3, 4, 5]:
                line2[pos - 3] = [chosen_symbol]
            else:
                line3[pos - 6] = [chosen_symbol]


    game_on()
    board()

    def keep_playing():
        yes_no = input("Do you want to keep playing? If so press y, if no choose n")
        while yes_no == 'y':
            print('Ok, lets play')
            tic_tac()
        else:
            try:
                while yes_no == 'n':
                    print('Nice game! See you next time')

                    break
            except yes_no not in ['n']:
                raise ValueError
                yes_no = input("Wrong value, If yes press y, if no choose n")

    keep_playing()


tic_tac()



