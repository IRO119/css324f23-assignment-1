import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)


def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res


def h3(s):
    # implement this function
    board, _, _ = s
    total = 0
    # this for loop looks to see if the board at a certain index is within the row target
    for idx in range(1, 9):
        if idx < 4:
            if (board[idx] != 1 or board[idx] != 2 or board[idx] != 3):
                total += 1
        elif idx < 7:
            if (board[idx] != 4 or board[idx] != 5 or board[idx] != 6):
                total += 1
        else:
            if (board[idx] != 7 or board[idx] != 8 or board[idx] != 0):
                total += 1

    # this for loop looks to see if the board at a certain index is within the column target
    for idx in range(1, 9):
        if idx < 4:
            if (board[idx] != 1 or board[idx] != 4 or board[idx] != 7):
                total += 1
        elif idx < 7:
            if (board[idx] != 2 or board[idx] != 5 or board[idx] != 8):
                total += 1
        else:
            if (board[idx] != 3 or board[idx] != 6 or board[idx] != 0):
                total += 1

    return total
