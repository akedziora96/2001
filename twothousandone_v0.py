import random


def twothousandone_v0():

    player_res, computer_res = 0, 0

    while player_res < 2001 and computer_res < 2001:

        input("You Turn. Press ENTER.")
        player_throw = random.randint(1, 6) + random.randint(1, 6)
        if player_throw == 7:
            player_res = player_res // 7
        elif player_throw == 11:
            player_res = player_res * 11
        else:
            player_res += player_throw

        computer_throw = random.randint(1, 6) + random.randint(1, 6)
        if computer_throw == 7:
            computer_res = computer_res // 7
        elif computer_throw == 11:
            computer_res = computer_res * 11
        else:
            computer_res += computer_throw

        if computer_res >= 2001:
            print('Computer won!')
        elif player_res >= 2001:
            print('Human won!')

        print(f"Player result: {player_res}, last throw: {player_throw}\n"
              f"Computer result: {computer_res}, last throw: {computer_throw}")


twothousandone_v0()
