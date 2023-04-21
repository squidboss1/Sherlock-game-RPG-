import random

detective_exp = 0
detective_level = 1
exp_for_level_2 = 100
exp_for_level_3 = 250
exp_for_level_4 = 400
exp_for_level_5 = 600

def response_pattern_1(right_answer, exp_to_gain=0):
    '''
    This is first response pattern for only 1 valid answer - a, b or c.
    After 3 wrong answers User will be informed about possibility of quit (type 'q')
    '''
    answer_abc = ''
    attemps = 0
    while answer_abc != right_answer:
        answer_abc = input("Type the solution (a, b or c): ")
        if answer_abc == right_answer:
            global detective_exp
            detective_exp += exp_to_gain
            print(f"\nWell done! You've earned {exp_to_gain} experience points. But be careful, the next questions will be more difficult and may be tricky.\n")
            print(f"You've got: {detective_exp} exp. points")

            # Print Experience level bar
            exp_level_bar(check_exp_for_next_level(), check_exp_for_subsequent_level())

            global detective_level
            print(
                f"To reach level {detective_level + 1} you need: {check_exp_for_next_level() - detective_exp} points more.\n")
            break
        if answer_abc == 'a' or answer_abc == 'b' or answer_abc == 'c' and answer_abc != right_answer:
            attemps += 1
            print("That\'s not quite truth. Try again.")
        elif answer_abc == 'q' or\
            answer_abc == 'z' or\
            answer_abc == 'w' or\
            answer_abc == 's' or\
            answer_abc == 'x' or\
            answer_abc == 'e' or\
            answer_abc == 'd' or\
            answer_abc == 'r' or\
            answer_abc == 'f' or\
            answer_abc == 'v' or\
            answer_abc == 't' or\
            answer_abc == 'g' or\
            answer_abc == 'n' or\
            answer_abc == 'y' or\
            answer_abc == 'h' or\
            answer_abc == 'u' or\
            answer_abc == 'j' or\
            answer_abc == 'm' or\
            answer_abc == 'i' or\
            answer_abc == 'k' or\
            answer_abc == 'l' or\
            answer_abc == 'o' or\
            answer_abc == 'p':
            attemps += 1
            print("You probably miss click. There is no such an answer. Try again.")
        elif answer_abc == '1' or\
             answer_abc == '2' or\
             answer_abc == '3' or\
             answer_abc == '4' or\
             answer_abc == '5' or\
             answer_abc == '6' or\
             answer_abc == '7' or\
             answer_abc == '8' or\
             answer_abc == '9' or\
             answer_abc == '0' or\
             answer_abc == '-' or\
             answer_abc == '=' or\
             answer_abc == ';' or\
             answer_abc == ',' or\
             answer_abc == '.' or\
             answer_abc == '/':
            attemps += 1
            print("You must be joking ;)")
        else:
            attemps += 1
            print("Try, you can do that.")

        # After 3 wrong answers user will be informed about possibility of quit
        if attemps == 3:
            x = input('If you want to quit game type \'q\'. Otherwise, you will be asked again for a solution. ')
            if x == 'q':
                exit()
            else:
                attemps = 0
            continue

        continue


def exp_level_bar(exp_for_next_level, exp_for_subsequent_level):
    '''
    Function prints Experience level bar.
    '''
    if detective_exp <= exp_for_next_level:
        proportions = (int(((detective_exp / exp_for_next_level) * 100) / 5))
        empty_spaces = 20 - proportions
        print(f'[', end='')
        print('x' * proportions, end='')
        print('-' * empty_spaces, end='')
        print(']')
    else:
        proportions = (int(((detective_exp / exp_for_subsequent_level) * 100) / 5))
        empty_spaces = 20 - proportions
        print(f'[', end='')
        print('x' * proportions, end='')
        print('-' * empty_spaces, end='')
        print(']')


def check_exp_for_next_level():
    '''
    Function returns experience value needed to achieve next level.
    '''
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
    '''
    Function returns experience value needed to achieve level after the next level.
    '''
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

def response_pattern_2(right_answer, wrong_answer, quit_answer, exp_to_gain=random.randint(5,20)):
    '''
        This is second response pattern for answers - a, b or c.
        One answer is right, one subtracts points, one leads to game over.
        '''
    answer_abc = input("Type the solution (a, b or c): ")
    if answer_abc == right_answer:
        global detective_exp
        detective_exp += exp_to_gain
        print(f"\nWell done! You've earned {exp_to_gain} experience points.\n")


        # Print Experience level bar
        exp_level_bar(check_exp_for_next_level(), check_exp_for_subsequent_level())

        global detective_level
        return print(f"To reach level {detective_level + 1} you need: {check_exp_for_next_level() - detective_exp} points more.\n")

    if answer_abc == wrong_answer:
        detective_exp -= exp_to_gain
        print(f"That\'s not quite polite. You lose {exp_to_gain} experience points. \n")
        print(f"You've got: {detective_exp} exp. points")

        # Print Experience level bar
        exp_level_bar(check_exp_for_next_level(), check_exp_for_subsequent_level())
        return

    if answer_abc == quit_answer:
        print("A true detective will not let go once started investigation.\n GAME OVER")
        return exit()