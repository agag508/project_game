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

player_one_symbol = input('Please choose o or x')

while player_one_symbol not in ['o', 'x']:
    player_one_symbol = input('Please choose a valid symbol o or x')
else:
    print("Thanks! You are going to play with {}".format(player_one_symbol))


def player_one():
    position_index = int(input("Hi! please choose the position you want to place your symbol"))
    while position_index not in range(9):
        position_index = int("Please choose a valid number between 0 and 8")

        if position_index in [0, 1, 2]:
            line1[position_index] = [player_one_symbol]
            print(line1[position_index])
        elif position_index in [3, 4, 5]:
            line2[position_index - 3] = [player_one_symbol]
            print(line2[position_index - 3])
        else:
            line3[position_index - 6] = [player_one_symbol]
            print(line3[position_index - 6])


player_one()

board()
