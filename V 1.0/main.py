import random
import os
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Igra Križić-Kružić s unosom dvaju korisnika - napredna verzija

def empty_board():
    return {1: ' ', 2: ' ', 3: ' ',
            4: ' ', 5: ' ', 6: ' ',
            7: ' ', 8: ' ', 9: ' '}

# Nasumično odabiremo znak (X ili O) za prvog igrača. Potom Prvi igrač ima potez.
def choose_player():
    pick = random.choice(["X", "O"])
    return pick, 'O' if pick == 'X' else 'X'

# Crtanje inicijalne ploče i nakon svakog poteza
def draw_board(board):
    clear_screen()
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("   |   |   \n")

def free_field(position, board):
    return board[position] == ' '

# Ovdje se vrši unos - naprednija verzija
def entry(board, sign, Player1, Player2):
    position = int(input("Choose the number of a field (1-9): "))
    if free_field(position, board):
        board[position] = sign
        clear_screen()
        draw_board(board)
        if match_draw(board):
            print("Draw!")
            return False
        if victory(sign, board):
            print(f"{sign} has won!")
            return False
        return True
    else:
        print("Chosen field is invalid. Try again.")
        return entry(board, sign, Player1, Player2)

# Definiramo neriješeni ishod
def match_draw(board):
    return all(value != ' ' for value in board.values())

# Definiramo uvjete pobjede
def victory(sign, board):
    for combo in [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                  (1, 4, 7), (2, 5, 8), (3, 6, 9),
                  (1, 5, 9), (7, 5, 3)]:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == sign:
            return True
    return False

def main():
    print("WELCOME TO 'TIC-TAC-TOE'\n")
    print("A rendition of the game by: Igor V. \n\n")  
    print("   |   |   ")
    print(" 1 | 2 | 3 ", )
    print("___|___|___")
    print(" 4 | 5 | 6 ", )
    print("___|___|___")
    print(" 7 | 8 | 9 ", )
    print("   |   |    \n")  
    sleep(2)

    # Petlja igre
    while True:
        board = empty_board()
        Player1, Player2 = "Player1", "Player2"
        current_player, opponent = choose_player()
        print(f"{current_player} goes first, {opponent} goes second.")
        sleep(1)
        draw_board(board)

        while True:
            if not entry(board, current_player, Player1, Player2):
                new_game = input("New game? (yes/no): ").strip().lower()
                if new_game == "no":
                    clear_screen()
                    print("Thank you for playing Tic Tac Toe.")
                    sleep(1)
                    exit()
                elif new_game == "yes":
                    break
                else:
                    print("Wrong entry.")
                    continue

            # Promjena igrača se vrši ovdje
            current_player, opponent = opponent, current_player

if __name__ == '__main__':
    main()
