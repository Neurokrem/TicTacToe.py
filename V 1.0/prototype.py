# Jednostavni prototip Križić Kružić

# Uvodni ekran
print("DOBRODOŠLI U IGRU 'KRIŽIĆ & KRUŽIĆ'\n")
print("A game by: Igor V. \n\n")    
print("   |   |   ")
print(" 1 | 2 | 3 ", )
print("___|___|___")
print(" 4 | 5 | 6 ", )
print("___|___|___")
print(" 7 | 8 | 9 ", )
print("   |   |   ")
print("\n")

# Ploča je niz znakova u listi.
board = [" ", " "," ",
         " ", " "," ",
         " ", " "," "]

# Uvjetujemo početne uvjete igre: prvo igra 'X', zatim igra 'O'
Player1 = "X"
Player2 = "O"
trenutno_igra = Player1
Igranje = True
pobjednik = None

def draw_board(board):
    print("\t " + board[0] + '|' + board[1] + '|' + board[2])
    print("\t_______")
    print("\t " + board[3] + '|' + board[4] + '|' + board[5])
    print("\t_______")
    print("\t " + board[6] + '|' + board[7] + '|' + board[8])
    print("\n")

# Unos igračâ
def unos_player(board):
    unos = int(input(f"Unesite znak u željeno polje (1-9): "))
    # Ovim uvjetima idemo po poljima i unosimo znak na određeno polje.
    if unos >= 1 and unos <= 9 and board[unos-1] == " ":
        board[unos-1] = trenutno_igra
    else:
        print("Polje je zauzeto. Molim unesite drugi broj.")

# Provjera uvjeta pobjede - prvo definiramo sve pobjedničke nizove, onda prizivamo funkciju provjere pobjednika
def provjera_vodoravno(board):
    # Nužna opasnost; provjeravamo uvjet pobjede preko cijelog  programa
    global pobjednik
    if board[0] == board[1] == board[2] and board[1] != " ":
    # nije bitno koje bolje odaberemo, na svakom je definiran pobjednik
        pobjednik = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != " ":
        pobjednik = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[7] != " ":
        pobjednik = board[6]
        return True
    
def provjera_okomito(board):
    global pobjednik
    if board[0] == board[3] == board[6] and board[0] != " ":
        pobjednik = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        pobjednik = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        pobjednik = board[2]
        return True

def provjera_dijagonala(board):
    global pobjednik
    if board[0] == board[4] == board[8] and board[0] != " ":
        pobjednik = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != " ":
        pobjednik = board[6]
        return True

def provjera_nerijeseno(board):
    global Igranje
    if " " not in board:
        draw_board(board)
        print("Neriješeno.")
        Igranje = False
        
# Definiranje pobjednika:
def pobjeda():
    if provjera_dijagonala(board) or provjera_okomito(board) or provjera_vodoravno(board):
        print(f"\n\n Pobijedio je {pobjednik}")
        
            

# Zamjena igrača - nužno za unos
def zamjena_igraca():
    global trenutno_igra
    if trenutno_igra == Player1:
        trenutno_igra = Player2
    else:
        trenutno_igra = Player1


while Igranje:
    draw_board(board=board)
    unos_player(board=board)
    pobjeda()
    provjera_nerijeseno(board)
    zamjena_igraca()

    if pobjednik:
        nova_igra = input("Nova igra? (da/ne): ").strip().lower()
        if nova_igra == "ne":
            break
        # Ovaj dio treba debugirat - ne iscrtava praznu ploču
        elif nova_igra == "da":
            board = [" ", " "," ",
                     " ", " "," ",
                     " ", " "," "]
            pobjednik = None 
            continue
        else:
            print("Krivi unos.")
            continue
           
print("Hvala što ste igrali Križić-Kružić.")
