#!/usr/bin/env python3

from numpy import random
import socket

# Localhost address and port number of column node to connect to 
HOST = '127.0.0.1'
PORT = 0

# Base values to be send to nodes
sendVal1 = ""
sendVal2 = ""
sendVal3 = ""

# Height of each column, can be changed to alter board height, width is fixed to 10
MAX_HEIGHT = 4

# Send the values to be input to one column
def sendPlay(column, values):
    PORT = 10000 + column
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(values.encode())
        s.close()

def readBoard():
    PORT = 10010

# In case of blocks reaching the top of the game board, clear the contents
# of each column node
def sendGameOver():
    values = ""
    for x in range(MAX_HEIGHT):
        values = values + "0"
    for x in range(3):
        PORT = 10000 + x
        print(PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(values.encode())
            s.close()

# Send block placement to server based on user selection of position
def playBlock(column, blockVal):

    # Values for determining height at which a block will be placed
    highestFilled = -1
    highestFilledS = -1
    toFill = 0

    # Case: User chooses column 0
    if column == 0:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column0[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                sendPlay(0, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column0[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column1[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column0[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column2[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendPlay(2, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column0[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column2[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendPlay(2, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column0[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendPlay(2, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column0[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column0[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column1[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendVal1 = ""
                sendVal2 = ""
        
        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column0[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column1[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column0[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column0[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                sendPlay(0, sendVal1)
                sendPlay(1, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 1
    if column == 1:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                sendPlay(1, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column3[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendPlay(3, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column4[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendPlay(3, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendPlay(3, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column1[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column1[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column1[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column1[x]
                sendPlay(1, sendVal1)
                sendPlay(2, sendVal2)
                sendVal1 = ""
                sendVal2 = ""
    
    # Case: User chooses column 2
    if column == 2:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                sendPlay(2, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column4[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendPlay(4, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column4[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendPlay(4, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendPlay(4, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column2[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column2[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column2[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column2[x]
                sendPlay(2, sendVal1)
                sendPlay(3, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 3
    if column == 3:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                sendPlay(3, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column5[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendPlay(5, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column5[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendPlay(5, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendPlay(5, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column3[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column3[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column3[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column3[x]
                sendPlay(3, sendVal1)
                sendPlay(4, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 4
    if column == 4:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                sendPlay(4, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column6[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendPlay(6, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column6[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendPlay(6, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendPlay(6, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column4[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column4[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column4[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column4[x]
                sendPlay(4, sendVal1)
                sendPlay(5, sendVal2)
                sendVal1 = ""
                sendVal2 = ""
    
    # Case: User chooses column 5
    if column == 5:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                sendPlay(5, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column7[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendPlay(7, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column7[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendPlay(7, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendPlay(7, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column5[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column5[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column5[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column5[x]
                sendPlay(5, sendVal1)
                sendPlay(6, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 6
    if column == 6:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                sendPlay(6, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column8[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column8[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendPlay(8, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column8[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendPlay(8, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column8[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendPlay(8, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column6[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column6[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column6[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column6[x]
                sendPlay(6, sendVal1)
                sendPlay(7, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 7
    if column == 7:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                sendPlay(7, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 8
    if column == 8:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                sendPlay(8, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

    # Case: User chooses column 9
    if column == 9:

        # Case: Block is an "I" piece
        if blockVal == 0:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 4):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                for x in range(MAX_HEIGHT):
                    if((x >= toFill) and x <= (toFill + 3)):
                        column9[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column9[x]
                sendPlay(9, sendVal1)
                sendVal1 = ""
        
        # Case: Block is an "O" piece
        if blockVal == 1:
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is a "T" piece
        if blockVal == 2:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is an "S" piece
        if blockVal == 3:
            for x in range(MAX_HEIGHT):
                if column7[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""

        # Case: Block is a "Z" piece
        if blockVal == 4:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column7[x] == "1" and x > (highestFilled + 1):
                    highestFilledS = x
            if((highestFilledS - highestFilled) <= 1):
                toFill = (highestFilled + 1)
            elif((highestFilledS - highestFilled) > 1):
                toFill = highestFilledS
            if toFill > (MAX_HEIGHT - 2):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal3 = sendVal3 + "1"
                    else:
                        sendVal3 = sendVal3 + column9[x]
                for x in range(MAX_HEIGHT):
                    if(x == toFill or x == (toFill + 1)):
                        column8[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x == (toFill + 1)):
                        column7[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column7[x]
                sendPlay(7, sendVal1)
                sendPlay(8, sendVal2)
                sendPlay(9, sendVal3)
                sendVal1 = ""
                sendVal2 = ""
                sendVal3 = ""
        
        # Case: Block is a "J" piece
        if blockVal == 5: 
            for x in range(MAX_HEIGHT):
                if column8[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column9[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

        # Case: Block is an "L" piece
        if blockVal == 6:
            for x in range(MAX_HEIGHT):
                if column9[x] == "1":
                    highestFilled = x
            for x in range(MAX_HEIGHT):
                if column8[x] == "1" and x > highestFilled:
                    highestFilled = x
            toFill = highestFilled + 1
            if toFill > (MAX_HEIGHT - 3):
                sendGameOver()
                exit(0)
            else:
                sendVal1 = ""
                sendVal2 = ""
                for x in range(MAX_HEIGHT):
                    if(x == toFill):
                        column9[x] = "1"
                        sendVal2 = sendVal2 + "1"
                    else:
                        sendVal2 = sendVal2 + column9[x]
                for x in range(MAX_HEIGHT):
                    if(x >= toFill and x <= (toFill + 2)):
                        column8[x] = "1"
                        sendVal1 = sendVal1 + "1"
                    else:
                        sendVal1 = sendVal1 + column8[x]
                sendPlay(8, sendVal1)
                sendPlay(9, sendVal2)
                sendVal1 = ""
                sendVal2 = ""

column0 = ["0","0","0","0"]
column1 = ["0","0","0","0"]
column2 = ["0","0","0","0"]
column3 = ["0","0","0","0"]
column4 = ["0","0","0","0"]
column5 = ["0","0","0","0"]
column6 = ["0","0","0","0"]
column7 = ["0","0","0","0"]
column8 = ["0","0","0","0"]
column9 = ["0","0","0","0"]

play = ""
blockVal = 0
netrominos = ["I","O","T","S","Z","J","L"]

while True:
    #blockVal = random.randint(3)
    blockVal = 6;
    for x in range(4):
        if(column0[x] == "1" and column1[x] == "1" and column2[x] == "1" and column3[x] == "1" and column4[x] == "1" and column5[x] == "1" and column6[x] == "1" and column7[x] == "1" and column8[x] == "1" and column9[x] == "1"):
            column0[x] = "0"
            column1[x] = "0"
            column2[x] = "0"
            column3[x] = "0"
            column4[x] = "0"
            column5[x] = "0"
            column6[x] = "0"
            column7[x] = "0"
            column8[x] = "0"
            column9[x] = "0"

    print("[" + column0[3] + "] " + "[" + column1[3] + "] " + "[" + column2[3] + "] " + "[" + column3[3] + "] " + "[" + column4[3] + "] " + "[" + column5[3] + "] " + "[" + column6[3] + "] " + "[" + column7[3] + "] " + "[" + column8[3] + "] " + "[" + column9[3] + "] ")
    print("[" + column0[2] + "] " + "[" + column1[2] + "] " + "[" + column2[2] + "] " + "[" + column3[2] + "] " + "[" + column4[2] + "] " + "[" + column5[2] + "] " + "[" + column6[2] + "] " + "[" + column7[2] + "] " + "[" + column8[2] + "] " + "[" + column9[2] + "] ")
    print("[" + column0[1] + "] " + "[" + column1[1] + "] " + "[" + column2[1] + "] " + "[" + column3[1] + "] " + "[" + column4[1] + "] " + "[" + column5[1] + "] " + "[" + column6[1] + "] " + "[" + column7[1] + "] " + "[" + column8[1] + "] " + "[" + column9[1] + "] ")
    print("[" + column0[0] + "] " + "[" + column1[0] + "] " + "[" + column2[0] + "] " + "[" + column3[0] + "] " + "[" + column4[0] + "] " + "[" + column5[0] + "] " + "[" + column6[0] + "] " + "[" + column7[0] + "] " + "[" + column8[0] + "] " + "[" + column9[0] + "] ")
    print("Next block: " + netrominos[blockVal])
    play = input("Which column would you like to place the block in? \n")
    if play == "0":
        playBlock(0, blockVal)
    if play == "1":
        playBlock(1, blockVal)
    if play == "2":
        playBlock(2, blockVal)
    if play == "3":
        playBlock(3, blockVal)
    if play == "4":
        playBlock(4, blockVal)
    if play == "5":
        playBlock(5, blockVal)
    if play == "6":
        playBlock(6, blockVal)
    if play == "7":
        playBlock(7, blockVal)
    if play == "8":
        playBlock(8, blockVal)
    if play == "9":
        playBlock(9, blockVal)
    