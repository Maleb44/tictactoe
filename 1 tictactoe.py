def print_table():
    lookup = ['-', 'X', 'O']
    for row in T:
        print ' '.join([lookup[cell] for cell in row])
    print


def move(player, row, column):
    global next_player

    row -= 1
    column -= 1

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



table_size = 4
winning_size = 2

T = [[0] * table_size for _ in range(table_size)]
next_player = 1

print_table()

move(1, 2, 2)
move(2, 3, 2)
move(1, 3, 3)
