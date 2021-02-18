DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION_COUNT = 4


def is_valid_column(col):
    col_size = 7
    idx = int(col)
    return 0 < idx <= col_size


def is_valid(r, c, multi_list):
    return 0 <= r < len(multi_list) and 0 <= c < len(multi_list[r])


def validate_input(input_given):
    if not isinstance(input_given, int):
        return 'Invalid input!'
    return input_given


def print_winner_message(player):
    print(f'The winner is player {player}')


def in_range(value, max_value):
    return 0 <= value < max_value


def is_win_condition_value(board, row_index, column_index, player, rows_count, columns_count):
    return in_range(row_index, rows_count) \
           and in_range(column_index, columns_count) \
           and board[row_index][column_index] == player


def has_win_condition(board, player, row_index, column_index, win_condition_count=DEFAULT_WIN_CONDITION_COUNT):
    rows_count = len(board)
    columns_count = len(board[0])
    left_horizontal_values = [
        is_win_condition_value(board, row_index, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]
    right_horizontal_values = [
        is_win_condition_value(board, row_index, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_vertical_values = [
        is_win_condition_value(board, row_index + d, column_index, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_vertical_values = [is_win_condition_value(board, row_index - d, column_index, player, rows_count, columns_count)
                          for d in range(win_condition_count)]

    down_left_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_right_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_left_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_right_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    results = [
        all(left_horizontal_values),
        all(right_horizontal_values),
        all(down_vertical_values),
        all(up_vertical_values),
        all(down_left_diagonal_values),
        all(down_right_diagonal_values),
        all(up_left_diagonal_values),
        all(up_right_diagonal_values)
    ]

    return any(results)
