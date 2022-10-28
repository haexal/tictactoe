from os import system, name
from array import *
from math import ceil
from random import randint


turn = "X"
game = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
win = False
winner = ""
mode = 0
tie = False
playAgain = "-"

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def checkWinCon():
    global win
    if win == False:
        checkRow()
    if win == False:
        checkLine()
    if win == False:
        checkDiagonal()

def checkTie():
    global tie
    global win
    win = True
    tie = True
    for i in range(3):
        for j in range(3):
            if game[i][j] == "-":
                tie = False
                win = False
                break
    


def checkLine():
    global win
    global winner
    for i in range(3):
        if (game[i][0] == game[i][1] == game[i][2] != "-"):
            winner = game[i][0]
            win = True

def checkRow():
    global win
    global winner
    for i in range(3):
        if (game[0][i] == game[1][i] == game[2][i] != "-"):
            winner = game[0][i]
            win = True

def checkDiagonal():
    global win
    global winner
    if (game[0][0] == game[1][1] == game[2][2]!= "-"):
        win = True
        winner = game[0][0]
    elif  (game[0][2] == game[1][1] == game[2][0]!= "-"):
        win = True
        winner = game[0][2]

def gameTime():
    global win, tie, turn, winner, game, playAgain, mode
    while mode != 1 and mode != 2:   
        clear()

        print(
"""
=================================
WELCOME TO THE GAME "TIC TAC TOE"
=================================

SELECT MODE :
1. 1-PLAYER
2. 2-PLAYER

""")

        mode = int(input())
        if mode != 1 and mode != 2:
            print("Please Select the correct mode")



    while win == False:
        clear()

        for x in game:
            print("| ", end="")
            for y in x:
                print(y, end=" | ")
            print("")

        checkWinCon()
        if win == False:
            checkTie()

        if win == False:
            if turn == "X":
                x = int(input("X's turn, pick from 1 - 9 : "))
                baris_x = ceil(x/3) - 1
                kolom_x = x % 3 - 1
                if game[baris_x][kolom_x] == '-':
                    game[baris_x][kolom_x] = "X"
                    turn = "O"
                else:
                    print("Sorry, try again!")
                    turn = "X"

            else:
                if mode == 2:
                    o = int(input("O's turn, pick from 1 - 9 : "))
                    baris_o = ceil(o/3) - 1
                    kolom_o = o % 3 - 1
                    if game[baris_o][kolom_o] == '-':
                        game[baris_o][kolom_o] = "O"
                        turn = "X"
                    else:
                        print("Sorry, try again!")
                        turn = "O"
                else:
                    o = randint(1, 9)
                    baris_o = ceil(o/3) - 1
                    kolom_o = o % 3 - 1
                    if game[baris_o][kolom_o] == '-':
                        game[baris_o][kolom_o] = "O"
                        turn = "X"
                    else:
                        print("Sorry, try again!")
                        turn = "O"

    if tie == False:
        print("THE WINNER IS", winner)
    else:
        print("TIE")
    PlayAgainAsk()


def PlayAgainAsk():
    global playAgain
    while playAgain != "Y" and playAgain != "y" and playAgain != "N" and playAgain != "n": 
        playAgain = input("Play Again Y/N... ")
        
    if (playAgain == "Y" or playAgain == "y"):
        reset()
        gameTime()

def reset():
    global win, tie, turn, winner, game, playAgain, mode
    turn = "X"
    game = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    win = False
    winner = ""
    mode = 0
    tie = False
    playAgain = "-"

gameTime()




