#!/usr/bin/env python3

"""
    This chapter features a Tic-Tac-Toe game. Tic-Tac-Toe is normally played
    with two people. One player is X and the other player is O. Players take
    turns placing their X or O. If a player gets three of their marks on the
    board in a row, column, or diagonal, they win. When the board fills up
    with neither player winning, the game ends in a draw.

    Для версии: Python 3.x.x

    Пример взят здесь:
            http://inventwithpython.com/invent4thed/chapter10.html
    Read online for free:
        "Invent Your Own Computer Games with Python, 4th Edition"
        Chapter 10
    Оригинальное решение :./InventWithPython_resources/tictactoe.py

    NOTE: I'm not speak English. The whole output (and comments) is
          translated by the  Google

          2018/08/11 00:38:52  не готово иногда провускает ходы

          #X - начинает и выигрывает???

          2018/08/11 09:45:04  Совсем не играет. Думать не хочеться.
          Первый день бросаю курить. Голову потихоньку сжимает.
"""

#########################  FUNCTION ###################################
def ShowBoard( board ):
    for i in range(1, len(board),3 ) :
        print( board[i] + '|' + board[i+1] + '|' + board[i+2] )
        if i<= 6 :
            print('-+-+-')

def GetPlayerMove( board ):
    print('What is your choise (1-9)')
    guess = input()
    if len(guess) == 1 and guess.isdigit():
        guess = int( guess )
        if board[guess]==' ' :
            board[guess] = 'X'
            return 0
        else :
            print('Oh, sheet')
            GetPlayerMove( board )
    return 1 #что-то пошло не так

def CheckCompWin( bd, lc) :
    # проверка на победную комбинацию
    # только прямые
    a = 1
    b = 4
    while b<=10 :
        c = 0
        for i in range(a,b) :
            if bd[i]==lc :
                c = c + 1
        if c == 2 :
            for i in range(a,b) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return 'WIN'
        a = a + 3
        b = b + 3

    # вертикаль
    a, b = 1, 8
    for x in range(1,4) :
        c = 0
        for i in range(a,b,3) :
            if bd[i]==' ' :
                c = c + 1
        if c == 2 :
            for i in range(a,b,3) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return 'WIN'
        a = a + 1
        b = b + 1

    #и диагональ
    c=0
    for i in range(1,10,4) :
        if bd[i]==lc :
                c = c + 1
        if c == 2 :
            for i in range(1,10,4) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return 'WIN'
    c = 0
    for i in range(3, 8, 2) :
        if bd[i]==lc :
                c = c + 1
        if c == 2 :
            for i in range(3, 8, 2) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return 'WIN'
    return 'KEK'

def CheckUserWin( bd, lc, lu) :
    # проверка на победную комбинацию
    
    a, b = 1, 4
    while b<=10 :
        c = 0
        # горизонт
        for i in range(a,b) :
            if bd[i]==lu :
                c = c + 1
        if c == 2 :
            for i in range(a,b) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return True
        a = a + 3
        b = b + 3

    # вертикаль
    a, b = 1, 8
    for x in range(1,4) :
            c = 0
            for i in range(a,b,3) :
                if bd[i]==lu :
                    c = c + 1
            if c == 2 :
                for i in range(a,b,3) :
                    if bd[i] == ' ' :
                        bd[i] = lc
                        return True
            a = a + 1
            b = b + 1

    #и диагональ
    c=0
    for i in range(1,10,4) :
        if bd[i]==lu :
                c = c + 1
        if c == 2 :
            for i in range(1,10,4) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return True
    c = 0
    for i in range(3, 8, 2) :
        if bd[i]==lu :
                c = c + 1
        if c == 2 :
            for i in range(3, 8, 2) :
                if bd[i] == ' ' :
                    bd[i] = lc
                    return True

def CheckCorner( bd, lc ) :
    if bd[1] == ' ' :
        bd[1]= lc
    elif bd[3] == ' ' :
        bd[3] = lc
    elif bd[7] == ' ' :
        bd[7] = lc
    elif bd[9] == ' ' :
        bd[9] == lc
    else :
        return False
    return True

def CheckSide( bd, lc ) :
    if bd[2] == ' ' :
        bd[2]= lc
    elif bd[4] == ' ' :
        bd[4] = lc
    elif bd[6] == ' ' :
        bd[6] = lc
    elif bd[8] == ' ' :
        bd[8] == lc
    else :
        return False
    return True

                    
def GetCompMove(bd, lc, lu):
    resCheck = CheckCompWin(bd, lc)
    if resCheck == 'WIN' :
        return 'WIN'
    resCheck = CheckUserWin(bd, lc, lu)
    if resCheck :
        return True

    if bd[5] == ' ' :
        bd[5]=lc
        return True
    resCheck = CheckCorner(bd, lc)
    if resCheck :
        return True
    resCheck = CheckSide( bd, lc )
    if resCheck :
        return True   
        

def CheckWon( board, le ) :  #lt - letter
    # If there are blank fields, further verification is meaningless
    if ((board[1] == le and board[2]== le and board[3] == le)
    or (board[4] == le and board[5]== le and board[6] == le)
    or (board[7] == le and board[8]== le and board[9] == le)
    or (board[1] == le and board[4]== le and board[7] == le)
    or (board[2] == le and board[5]== le and board[8] == le)
    or (board[3] == le and board[6]== le and board[9] == le)
    or (board[1] == le and board[5]== le and board[9] == le)
    or (board[3] == le and board[5]== le and board[7] == le)) :
        return 'WON'
    elif ' ' not in board :
        return 'TIE' # I have one option - it's a draw

    
#########################   START   ##################################
####### ПОДГОТОВКА ПЕРЕМЕННЫХ ###
#X - начинает и выигрывает???
playerLetter  = 'X'
compLetter    = 'O'

board = ['Z',' ',' ',' ',' ',' ',' ',' ',' ',' ']


         
boardHelp = """1|2|3
               -+-+-
               4|5|6
               -+-+-
               7|8|9 """

while True:               
    ShowBoard( board )
    GetPlayerMove(board)
    resultCheck = CheckWon(board, playerLetter)
    
    if resultCheck == 'WON' :
        playerLetter = 'WON'
        break
    elif resultCheck == 'TIE' : #def CheckTie() #ходов может быть не боьше девяти
        playerLetter = 'TIE'
        break

    GetCompMove(board, compLetter, playerLetter)
    
    resultCheck = CheckWon(board, compLetter)
    print(board)
    if resultCheck == 'WON' :
        playerLetter = 'LOSE'
        break
    elif resultCheck == 'TIE' : #def CheckTie() #ходов может быть не боьше девяти
        playerLetter = 'TIE'
        break

ShowBoard( board )
print(playerLetter)
#    print('You won congratulations')
