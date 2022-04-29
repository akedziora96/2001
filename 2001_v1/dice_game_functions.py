import random


def code_to_dices(key):

    DICE_DIC = {'D3': 3, 'D4': 4, 'D6': 6, 'D8': 8, 'D10': 10, 'D12': 12, 'D20': 20, 'D100': 100}

    try:
        if key not in DICE_DIC:
            return None
        else:
            return DICE_DIC[key]
    except (TypeError, KeyError):
        return None


def player_choice():

    is_1dice_exists = False
    is_2dice_exists = False

    while not is_1dice_exists:
        player_input_1 = input('Choose first dice: ').upper()
        if code_to_dices(player_input_1) is None:
            print("Wrong dice code!")
            continue
        else:
            player_dice_1 = code_to_dices(player_input_1)
            is_1dice_exists = True

    while not is_2dice_exists:
        player_input_2 = input('Choose second dice: ').upper()
        if code_to_dices(player_input_2) is None:
            print("Wrong dice code!")
            continue
        else:
            player_dice_2 = code_to_dices(player_input_2)
            is_2dice_exists = True

    return player_dice_1, player_dice_2


def computer_choice():

    DICES_TO_PLAY = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')

    computer_dice_1 = code_to_dices(random.choice(DICES_TO_PLAY))
    computer_dice_2 = code_to_dices(random.choice(DICES_TO_PLAY))

    return computer_dice_1, computer_dice_2
