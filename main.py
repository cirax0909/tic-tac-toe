def printBoard(board):
    print(board['7'] + '|' + board["8"] + '|' + board["9"])
    print('-+-+-')
    print(board["4"] + '|' + board["5"] + '|' + board["6"])
    print('-+-+-')
    print(board["1"] + '|' + board["2"] + '|' + board["3"])


def player(le):
    while True:
        player_move = input(f" {le} please choose the position you want for this turn (1 to 9):")
        try:
            player_move = int(player_move)
            if 9 >= player_move > 0:
                if theBoard[f'{player_move}'] == " ":
                    theBoard[f'{player_move}'] = f"{le}"
                    break
                elif theBoard[f'{player_move}'] == " ":
                    theBoard[f'{player_move}'] = f"{le}"
                    break
                else:
                    print("This position is occupied!")
            else:
                print("Please enter a number from 1 to 9.")
        except:
            print("Please enter a number only!")


def check_Winner(le):
    if (theBoard["7"] == le and theBoard["8"] == le and theBoard["9"] == le and le != ' ') or \
            (theBoard["4"] == le and theBoard["5"] == le and theBoard["6"] == le and le != ' ') or \
            (theBoard["1"] == le and theBoard["2"] == le and theBoard["3"] == le and le != ' ') or \
            (theBoard["7"] == le and theBoard["4"] == le and theBoard["1"] == le and le != ' ') or \
            (theBoard["8"] == le and theBoard["5"] == le and theBoard["2"] == le and le != ' ') or \
            (theBoard["9"] == le and theBoard["6"] == le and theBoard["3"] == le and le != ' ') or \
            (theBoard["7"] == le and theBoard["5"] == le and theBoard["3"] == le and le != ' ') or \
            (theBoard["9"] == le and theBoard["5"] == le and theBoard["1"] == le and le != ' '):
        return le


def check_blank():
    if ' ' not in theBoard.values():
        print("Draw")
        return False
    else:
        return True


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
while True:
    printBoard(theBoard)
    player("X")
    if check_blank():
        printBoard(theBoard)
        if check_Winner("X") == "X":
            print("Player 1 won.")
            break

        elif player("O"):
            if check_Winner("O") == "O":
                printBoard(theBoard)
                print("Play 2 won.")
                break
    else:
        break
