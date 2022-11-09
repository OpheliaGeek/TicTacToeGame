from random import shuffle
import os
os.system("cls")
"""
Simple TicTacToe game
"""
# global variables
WINNER = " "
GAME_FIELD = {"1": " ", "2": " ", "3": " ", "4": " ",
              "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
PLAYER_1 = ""
PLAYER_2 = ""


def welcome():
    """
    Function to welcome and show games's rules
    """
    print("""
    ================================================
    =======    Welcome to Tic Tac Toe Game    ======
    ================================================
    === Game rules:
    === 1. Game should play two players. 
    === 2. Before start game will flip coin to show who will start.
           Players could choose side: H for "Heads" or T for "Tails"
           Player who won will start with "X" symbol.
    === 3. On screen players will see field 3x3 to place their symboles.
           For navigate throw field, please, use numpad numbers from 1 to 9.
           Example:
             =====  =====  =====
            |  7  ||  8  ||  9  |
             =====  =====  ===== 
            |  4  ||  5  ||  6  |
             =====  =====  ===== 
            |  1  ||  2  ||  3  |
             =====  =====  ===== 
    
    === 4. Then each players will place their symboles on field (one per turn )
    === 5. The first player to draw three of their symbols in a row, 
           whether it is horizontal, vertical, or diagonal, has won tic-tac-toe.

    ==================================================
    ========    Good Luck and Have fun    ============ 
    ==================================================
    """)


def enter_key():
    """
    funtion which will wait until person will press "Enter"
    """
    input("Press Enter to continue....")


def flip_coin():
    """
    function which will flip coin and result will show player who will start first
    """
    roll = ["H", "T"]    # list of values
    shuffle(roll)        # shuffle list
    winner_coin = roll[0]     # first letter will be WINNER
    global PLAYER_1      # result of this function will change global values of players
    global PLAYER_2
    while True:         # loop will ask letters until input will meet requers
        PLAYER_1 = input(
            "Please choose H for 'Heads' or T for 'Tails', WINNER will start first, with 'X' symbol: ")
        if PLAYER_1 in ("H", "T"):
            print(f"Player_1 chose: {PLAYER_1}")
            # after pleyer 1 will choose letter, this letter will be deleted from list and secnond will get another from the list
            roll.pop(roll.index(PLAYER_1))
            PLAYER_2 = str(roll[0])
            print(f"PLAYER_2 will be: {PLAYER_2}")
            break
        else:
            # if letter not exist in list programm will ask again for right one
            print("Not in List. Try again")
    print(f"After flipping.... the coin shows: ==== {winner_coin} ====")
    # this part will change global values of PLAYER_1 and PLAYER_2 and annonce WINNER
    if PLAYER_1 == winner_coin:
        print(" ------ > Player_1 won and will start first with symbol 'X' <-------")
        PLAYER_1 = "X"
        PLAYER_2 = "O"
    else:
        print(" ------ > PLAYER_2 won and will start first with symbol 'X' <-------")
        PLAYER_1 = "O"
        PLAYER_2 = "X"
    return PLAYER_1, PLAYER_2


def show_game_field():
    """
    Function to clear terminal and show game field with last update 
    """
    os.system("cls")
    print(f"""

             =====  =====  =====
            |  {GAME_FIELD["7"]}  ||  {GAME_FIELD["8"]}  ||  {GAME_FIELD["9"]}  |
             =====  =====  =====
            |  {GAME_FIELD["4"]}  ||  {GAME_FIELD["5"]}  ||  {GAME_FIELD["6"]}  |
             =====  =====  =====
            |  {GAME_FIELD["1"]}  ||  {GAME_FIELD["2"]}  ||  {GAME_FIELD["3"]}  |
             =====  =====  =====
             """)


os.system("cls")  # clear terminal before game starts
welcome()  # rules
enter_key()  # wait for players
os.system("cls")  # clear terminal
flip_coin()  # mini game to change values of global variables
enter_key()  # wait for players
os.system("cls")  # clear terminal
if PLAYER_1 == "X":  # announce before game starts
    print("===== Player_1 first turn =====")
else:
    print("===== PLAYER_2 first turn =====")
enter_key()  # wait for players

while WINNER != "X" != "O" != 0:  # loop will work until one of player win or 0 means field dont have empty space and we have no WINNER
    for turn in ("X", "O"):  # "X" will start first and then change to "O"
        show_game_field()  # show game field

        # prgramm will ask for number to place in field symbol if input correct, if there is no space programm will ask another number
        while True:
            player_turn = str(input(" Choose number from 1 to 9:   "))
            if player_turn in (GAME_FIELD.keys()) and GAME_FIELD[player_turn] == " ":
                GAME_FIELD[player_turn] = turn
                break   # continue to check WINNER
            else:
                print("This space already used or number isn't between 1 to 9.")

        # this part will check WINNER combination

        for check in GAME_FIELD.keys():
            # 3 horazental lines
            if int(check) % 3 == 0 and GAME_FIELD[check] != " " and GAME_FIELD[check] == GAME_FIELD[str(int(check)-1)] == GAME_FIELD[str(int(check)-2)]:
                WINNER = turn  # value of WINNER will take value of which symbol have win combination
                break
            # 3 vertical lines
            elif int(check) < 4 and GAME_FIELD[check] != " " and GAME_FIELD[check] == GAME_FIELD[str(int(check)+3)] == GAME_FIELD[str(int(check)+6)]:
                WINNER = turn
                break
            # first giagonal
            elif int(check) == 1 and GAME_FIELD[check] != " " and GAME_FIELD[check] == GAME_FIELD[str(int(check)+4)] == GAME_FIELD[str(int(check)+8)]:
                WINNER = turn
                break
            # second giagonal
            elif int(check) == 3 and GAME_FIELD[check] != " " and GAME_FIELD[check] == GAME_FIELD[str(int(check)+2)] == GAME_FIELD[str(int(check)+4)]:
                WINNER = turn
                break
            # if field dont have anymore space that means we dont have WINNER
            elif " " not in list(GAME_FIELD.values()):
                WINNER = 0
                break
        if WINNER != " ":  # after we get WINNER or no winners we stop checking combinations
            break
    if WINNER != " ":  # after we get einner we stop asking for new numbers
        break

# we show last update of the field and annonce WINNER
show_game_field()
if WINNER == PLAYER_1:
    print(f"========= WINNER PLAYER_1 {PLAYER_1} ===========")
if WINNER == PLAYER_2:
    print(f"========= WINNER PLAYER_2 {PLAYER_2}===========")
if WINNER == 0:
    print("========= NOBODY WINS! ===========")
