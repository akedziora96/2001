from dice_game_functions import player_choice, computer_choice
import random


def twothousandone_v1():

    print("Chose between dices: 'D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100'")

    player_res, computer_res = 0, 0

    while player_res < 2001 and computer_res < 2001:

        c_max_dice_1, c_max_dice_2 = computer_choice()
        p_max_dice_1, p_max_dice_2 = player_choice()

        player_throw = random.randint(1, p_max_dice_1) + random.randint(1, p_max_dice_2)
        if player_throw == 7:
            player_res = player_res // 7
        elif player_throw == 11:
            player_res = player_res * 11
        else:
            player_res += player_throw

        computer_throw = random.randint(1, c_max_dice_1) + random.randint(1, c_max_dice_2)
        if computer_throw == 7:
            computer_res = computer_res // 7
        elif computer_throw == 11:
            computer_res = computer_res * 11
        else:
            computer_res += computer_throw

        if computer_res >= 2001:
            print('Computer won!')
        elif player_res >= 2001:
            print('Player won!')

        print(f"Player result: {player_res}, last throw: {player_throw}\n"
              f"Computer result: {computer_res}, last throw: {computer_throw}")


if __name__ == '__main__':
    twothousandone_v1()
