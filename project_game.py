board_lines = []

line1 = [[0], [1], [2]]
line2 = [[3], [4], [5]]
line3 = [[6], [7], [8]]

board_lines = [line1, line2, line3]


def board():
    for line in board_lines:
        print(line)
    return board_lines


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
    position_index = int(input("Please choose the position you want to place your symbol"))
    while position_index not in range(9):
        position_index = int(input("Please choose a valid number between 0 and 8"))
    else:
        if position_index in [0, 1, 2]:
            line1[position_index] = [chosen_symbol]
            """print( line1[position_index]) prints individual cell)"""
        elif position_index in [3, 4, 5]:
            line2[position_index - 3] = [chosen_symbol]
        else:
            line3[position_index - 6] = [chosen_symbol]


game_on()
board()

def keep_playing():
    yes_no = input("Do you want to keep playing? If so press y, if no choose n")
    while yes_no not in ['y', 'n', 'Y', 'N']:
        yes_no = input("Invalid input, please choose y or n.")
    else:
       try:
           yes_no in ['y','Y']

       except yes_no =='n':
           raise ValueError
       else:
           return symbol_pick()






keep_playing()
game_on()
board()
