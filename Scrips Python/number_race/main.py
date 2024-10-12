"""
scrip description: Numer race
Dev: Christian G.
Date: 13/09/2024
"""

from random import randint
import os

status_menu = True


def main_menu():
    global status_opts
    status_opts = True
    print(":::::MAIN MENU:::::")
    print("[1]. Star Game")
    print("[2]. Help")
    print("[3]. Exit")

    while status_opts:
        opt = int(input("Press any option: "))
        if opt < 1 or opt > 3:
            print("Error. Press any option between 1 and 3")
        else:
            status_opts = False
    return opt


while status_menu:
    os.system("clear")
    main_menu()
    op = main_menu()
    if op == 1:
        os.system("clear")
        print("Game Under Construction")

        players = int(input("Press number of players [1:4]"))

        print(":::::: Level Menu :::::")
        print("[1]. Basic")
        print("[2]. Intermediate")
        print("[3]. Advance")
        print("[4]. Expert")
        opt = int(input("Press any option: "))

        if opt == 1:
            pos == 20
        elif opt == 2:
            pos = 30
        elif opt == 3:
            pos = 50
        else:
            pos = 100

        # Star game
        status_game = True
        roll_count = 0
        roll_acum = 0
        while status_game:
            key = input("Press any key to roll dice ...")

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(f"Dice 1:{dice1}")
            print(f"Dice 2:{dice2}")
            total = dice1 + dice2
            print(f"Total: {total}")

            roll_count += 1
            roll_acum += total
            print(f"Acum: {roll_acum}")

            if roll_acum >= pos:
                print("   ******* YOU WIN! *******")
                print("*******CONGRATULATIONS *******")
                status_game = False

            os.system("pause")

        print("   ::::: STATICS :::::")
        print(f"Total rolls: {roll_count}")
        print(f"Total Dices: {roll_acum}")

        key = input("Press any to go to the main menu...")
    elif op == 2:
        print("Help Under Construction")
        key = input("Press any to go to the main menu...")
    else:
        print("See 'u later")
        key = input("Press any ket to exit")
        break
