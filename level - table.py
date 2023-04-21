
detective_exp = 0
detective_level = 1
exp_for_level_2 = 100
exp_for_level_3 = 250
exp_for_level_4 = 400
exp_for_level_5 = 600

def exp_level_bar(exp_for_next_level, exp_for_subsequent_level):
    if detective_exp <= exp_for_next_level:
        proporcions = (int(((detective_exp / exp_for_next_level) * 100) / 5))
        empty_spaces = 20 - proporcions
        print(f'[', end='')
        print('x' * proporcions, end='')
        print('-' * empty_spaces, end='')
        print(']')
    else:
        proporcions = (int(((detective_exp / exp_for_subsequent_level) * 100) / 5))
        empty_spaces = 20 - proporcions
        print(f'[', end='')
        print('x' * proporcions, end='')
        print('-' * empty_spaces, end='')
        print(']')


def check_exp_for_next_level():
    exp_for_next_level = 0
    if detective_level == 1:
        exp_for_next_level = exp_for_level_2
    elif detective_level == 2:
        exp_for_next_level = exp_for_level_3
    elif detective_level == 3:
        exp_for_next_level = exp_for_level_4
    elif detective_level == 4:
        exp_for_next_level = exp_for_level_5
    return exp_for_next_level

def check_exp_for_subsequent_level():
    exp_for_subsequent_level = 0
    if detective_level == 1:
        exp_for_subsequent_level = exp_for_level_3
    elif detective_level == 2:
        exp_for_subsequent_level = exp_for_level_4
    elif detective_level == 3:
        exp_for_subsequent_level = exp_for_level_5
    elif detective_level == 4:
        exp_for_subsequent_level = 1000
    return exp_for_subsequent_level

exp_level_bar(check_exp_for_next_level(), check_exp_for_subsequent_level())

