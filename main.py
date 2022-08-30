def printBoard(board):
    print(board['7'] + '|' + board["8"] + '|' + board["9"])
    print('-+-+-')
    print(board["4"] + '|' + board["5"] + '|' + board["6"])
    print('-+-+-')
    print(board["1"] + '|' + board["2"] + '|' + board["3"])


def player1():
    while True:
        player1_move = input("X please choose the position you want for this turn (1 to 9):")
        try:
            player1_move = int(player1_move)
            if 9 > player1_move > 0:
                if theBoard[f'{player1_move}'] == " ":
                    theBoard[f'{player1_move}'] = "X"
                    break
                else:
                    print("This position is occupied!")
            else:
                print("Please enter a number from 1 to 9.")
        except:
            print("Please enter a number only!")


def player2():
    while True:
        player2_move = input("O please choose the position you want for this turn (1 to 9):")
        try:
            player2_move = int(player2_move)
            if 9 >= player2_move > 0:
                if theBoard[f'{player2_move}'] == " ":
                    theBoard[f'{player2_move}'] = "O"
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
        (theBoard["8"] == le and theBoard["5"] == le and theBoard["2"] == le and le != ' ') or\
        (theBoard["9"] == le and theBoard["6"] == le and theBoard["3"] == le and le != ' ') or \
        (theBoard["7"] == le and theBoard["5"] == le and theBoard["3"] == le and le != ' ') or \
        (theBoard["9"] == le and theBoard["5"] == le and theBoard["1"] == le and le != ' '):
        return le
    else:
        return 1


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}
while True:
    printBoard(theBoard)
    player1()
    printBoard(theBoard)
    player2()
    if check_Winner("X") == "X":
        print("Player 1 won.")
        break
    elif check_Winner("X") == "O":
        print("Play 2 won.")
        break
    else:
        print("Draw")
