import random


def print_table():
    lookup = ['-', 'X', 'O']
    for row in T:
        print ' '.join([lookup[cell] for cell in row])
    print


def move(player, row, column):
    global next_player

    assert player == next_player, 'player not valid'
    assert row in range(table_size), 'row out of range'
    assert column in range(table_size), 'column out of range'
    assert T[row][column] == 0, 'avoid illegal move'

    T[row][column] = player   # writing to global variable, why is not a problem,

    lookup_next_player = {
        1: 2,
        2: 1
    }
    next_player = lookup_next_player[next_player]

    print_table()

    state = game_state()
    if state in [1, 2]:
        print 'winner: {}'.format(state)

    if state == 3:
        print 'draw'



def game_state():
    directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    can_continue = False

    for row in range(table_size):
        for column in range(table_size):
            for dir_x, dir_y in directions:
                p = check_cell(row, column, dir_x, dir_y)
                if p:
                    return p

            if T[row][column] == 0:
                can_continue = True

    if can_continue:
        return 0     # can continue

    return 3     # draw



def check_cell(row, column, dir_x, dir_y):
    cell = T[row][column]

    if cell == 0:
        return 0

    # if not (0 <= column + dir_x * winning_size <= table_size):
        # return 0

    if column + dir_x * winning_size not in range(table_size):
        return 0

    if row + dir_y * winning_size not in range(table_size):
        return 0

    for i in range(1, winning_size):
        if T[row + (i * dir_y)][column + (i * dir_x)] != cell:
            return 0

    return cell


def ask_names_confirm():
    for i in ['first', 'second']:
        confirm = ''
        while confirm not in ['yes', 'y']:
            name = raw_input('What is {} player\'s name? '
                             .format(i)).strip().title()
            confirm = raw_input('Are you "{}", is this correct? [yes/no] '
                            .format(name)).strip().lower()
        players.append(name)


def first_player():
    global next_player
    next_player = random.randint(0, 1)
    print 'First player is: {}'.format(players[next_player])


def play():
    answer = raw_input('{} where do you move? "row column": '
                       .format(players[next_player]))

    # HOMEWORK

# constants
table_size = 4
winning_size = 2

# globals
T = [[0] * table_size for _ in range(table_size)]
players = []
next_player = -1

# script
ask_names_confirm()
first_player()
print_table()
play()

