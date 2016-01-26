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
    can_continue = False

    for row in range(table_size):
        for column in range(table_size):
            p = check_state_horizontal_start(row, column)
            if p:
                return p

            p = check_state_vertical_start(row, column)
            if p:
                return p

            p = check_state_diag_se_start(row, column)
            if p:
                return p

            p = check_state_diag_sw_start(row, column)
            if p:
                return p

            if T[row][column] == 0:
                can_continue = True


    if can_continue:
        return 0     # can continue

    return 3     # draw



def check_state_horizontal_start(row, column):
    cell = T[row][column]

    if cell == 0:
        return 0

    if column + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row][column + i] != cell:
            return 0

    return cell


def check_state_vertical_start(row, column):
    cell = T[row][column]
    if row + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column] != cell:
            return 0

    return cell


def check_state_diag_se_start(row, column):
    cell = T[row][column]
    if row + winning_size > table_size or \
            column + winning_size > table_size:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column + i] != cell:
            return 0

    return cell



def check_state_diag_sw_start(row, column):
    cell = T[row][column]
    if row + winning_size > table_size or \
            column - winning_size < 0:
        return 0

    for i in range(1, winning_size):
        if T[row + i][column - i] != cell:
            return 0

    return cell




table_size = 4
winning_size = 2

T = [[0] * table_size for _ in range(table_size)]
next_player = 1

print_table()

move(1, 3, 3)
move(2, 1, 1)
move(1, 3, 4)
move(2, 2, 3)
