from random import choice
from advanced.workshop.game_connect_four.field import new_field, print_field, get_initial_state_dept
from advanced.workshop.game_connect_four.player import Player

from advanced.workshop.game_connect_four.validations import is_valid_column, has_win_condition, print_winner_message

DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION_COUNT = 4
player_one = Player('Dean', 1)
player_two = Player('Simona', 2)
players = [player_one, player_two]


def play():
    game_field = new_field()
    start_dept = get_initial_state_dept()
    next_player_to_move = choice(players)
    while True:
        current_dept = start_dept
        print(f'Player {next_player_to_move.name}, please choose a column')

        column_number = input()
        if column_number is '' or not is_valid_column(column_number):
            print(f'Invalid column!\nPlayer {next_player_to_move.name}, please choose again.')
            column_number = int(input())

        col_idx = int(column_number) - 1
        row_idx = current_dept[col_idx]
        game_field[row_idx][col_idx] = next_player_to_move.start_number
        current_dept[col_idx] -= 1

        print_field(game_field)
        if has_win_condition(game_field, next_player_to_move.start_number, row_idx, col_idx):
            print_winner_message(next_player_to_move.name)
            break

        if next_player_to_move.name == player_one.name:
            next_player_to_move = player_two
        else:
            next_player_to_move = player_one

    new_game()


def new_game():
    print('Do you want another Game?\n(Y, N)')
    answer = input().lower()
    if answer == 'y':
        play()
    else:
        print('Goodbye!')
