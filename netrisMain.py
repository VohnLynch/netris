#!/usr/bin/env python3

from numpy import random
import socket
import threading
import subprocess
import time


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

# Series of subprocess functions that run each of the 10 servers upon startup
def col0():
    subprocess.run(['python', 'column0.py'])

def col1():
    subprocess.run(['python', 'column1.py'])

def col2():
    subprocess.run(['python', 'column2.py'])

def col3():
    subprocess.run(['python', 'column3.py'])

def col4():
    subprocess.run(['python', 'column4.py'])

def col5():
    subprocess.run(['python', 'column5.py'])

def col6():
    subprocess.run(['python', 'column6.py'])

def col7():
    subprocess.run(['python', 'column7.py'])

def col8():
    subprocess.run(['python', 'column8.py'])

def col9():
    subprocess.run(['python', 'column9.py'])

def read0():
    subprocess.run(['python', 'read0.py'])

def read1():
    subprocess.run(['python', 'read1.py'])

def read2():
    subprocess.run(['python', 'read2.py'])

def read3():
    subprocess.run(['python', 'read3.py'])

def read4():
    subprocess.run(['python', 'read4.py'])

def read5():
    subprocess.run(['python', 'read5.py'])

def read6():
    subprocess.run(['python', 'read6.py'])

def read7():
    subprocess.run(['python', 'read7.py'])

def read8():
    subprocess.run(['python', 'read8.py'])

def read9():
    subprocess.run(['python', 'read9.py'])

# Create a set of 10 threads and start the servers
c0 = threading.Thread(target = col0)
c1 = threading.Thread(target = col1)
c2 = threading.Thread(target = col2)
c3 = threading.Thread(target = col3)
c4 = threading.Thread(target = col4)
c5 = threading.Thread(target = col5)
c6 = threading.Thread(target = col6)
c7 = threading.Thread(target = col7)
c8 = threading.Thread(target = col8)
c9 = threading.Thread(target = col9)
r0 = threading.Thread(target = read0)
r1 = threading.Thread(target = read1)
r2 = threading.Thread(target = read2)
r3 = threading.Thread(target = read3)
r4 = threading.Thread(target = read4)
r5 = threading.Thread(target = read5)
r6 = threading.Thread(target = read6)
r7 = threading.Thread(target = read7)
r8 = threading.Thread(target = read8)
r9 = threading.Thread(target = read9)
c0.start()
c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()
c7.start()
c8.start()
c9.start()
r0.start()
r1.start()
r2.start()
r3.start()
r4.start()
r5.start()
r6.start()
r7.start()
r8.start()
r9.start()


# Localhost address and port number of column node to connect to 
HOST = '127.0.0.1'
PORT = 0

# Base values to be sent to nodes
sendVal1 = ""
sendVal2 = ""
sendVal3 = ""

# Height of each column, can be changed to alter board height, width is fixed to 10
MAX_HEIGHT = 4

# Send the values to be input to one column
def sendPlay(column, values):
    if column >= 10:
        column = column - 10
    PORT = 10000 + column
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(values.encode())
        s.close()

# Connect to reading servers, input data into local board storage
def getBoard():
    values = "GET"
    for x in range(10):
        PORT = 10010 + x
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(values.encode())
            data = s.recv(1024).decode()
            if x == 0:
                for i in range(MAX_HEIGHT):
                    column0[i] = data[i]
            
            if x == 1:
                for i in range(MAX_HEIGHT):
                    column1[i] = data[i]
            if x == 2:
                for i in range(MAX_HEIGHT):
                    column2[i] = data[i]
            
            if x == 3:
                for i in range(MAX_HEIGHT):
                    column3[i] = data[i]
            
            if x == 4:
                for i in range(MAX_HEIGHT):
                    column4[i] = data[i]
            
            if x == 5:
                for i in range(MAX_HEIGHT):
                    column5[i] = data[i]
            
            if x == 6:
                for i in range(MAX_HEIGHT):
                    column6[i] = data[i]
            
            if x == 7:
                for i in range(MAX_HEIGHT):
                    column7[i] = data[i]
            
            if x == 8:
                for i in range(MAX_HEIGHT):
                    column8[i] = data[i]
            
            if x == 9:
                for i in range(MAX_HEIGHT):
                    column9[i] = data[i]
            s.close()

# In case of blocks reaching the top of the game board, clear the contents
# of each column node
def sendGameOver():
    values = ""
    for x in range(MAX_HEIGHT):
        values = values + "0"
    for x in range(10):
        PORT = 10000 + x
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(values.encode())
            s.close()
    values = "END"
    for x in range(20):
        PORT = 10000 + x
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(values.encode())
            s.close()
    print("Game over!")
    exit(0)

def deleteRows():
    values0 = values1 = values2 = values3 = values4 = values5 = values6 = values7 = values8 = values9 = ""
    for x in range(MAX_HEIGHT):
        if column0[x] == column1[x] == column2[x] == column3[x] == column4[x] == column5[x] == column6[x] == column7[x] == column8[x] == column9[x] == "1":
            for i in range(MAX_HEIGHT):
                if i < x:
                    values0 = values0 + column0[i]
                    values1 = values1 + column1[i]
                    values2 = values2 + column2[i]
                    values3 = values3 + column3[i]
                    values4 = values4 + column4[i]
                    values5 = values5 + column5[i]
                    values6 = values6 + column6[i]
                    values7 = values7 + column7[i]
                    values8 = values8 + column8[i]
                    values9 = values9 + column9[i]
                elif i >= x and i != MAX_HEIGHT - 1:
                    values0 = values0 + column0[i + 1]
                    values1 = values1 + column1[i + 1]
                    values2 = values2 + column2[i + 1]
                    values3 = values3 + column3[i + 1]
                    values4 = values4 + column4[i + 1]
                    values5 = values5 + column5[i + 1]
                    values6 = values6 + column6[i + 1]
                    values7 = values7 + column7[i + 1]
                    values8 = values8 + column8[i + 1]
                    values9 = values9 + column9[i + 1]
                elif i >= x and i == MAX_HEIGHT - 1:
                    values0 = values0 + "0"
                    values1 = values1 + "0"
                    values2 = values2 + "0"
                    values3 = values3 + "0"
                    values4 = values4 + "0"
                    values5 = values5 + "0"
                    values6 = values6 + "0"
                    values7 = values7 + "0"
                    values8 = values8 + "0"
                    values9 = values9 + "0"
            sendPlay(0, values0)
            sendPlay(1, values1)
            sendPlay(2, values2)
            sendPlay(3, values3)
            sendPlay(4, values4)
            sendPlay(5, values5)
            sendPlay(6, values6)
            sendPlay(7, values7)
            sendPlay(8, values8)
            sendPlay(9, values9)
            getBoard()
                    

# Send block placement to server based on user selection of position
def playBlock(playColumn0, playColumn1, playColumn2, blockVal, play):

    # Values for determining height at which a block will be placed
    highestFilled = -1
    highestFilledS = -1
    toFill = 0

    # Case: Block is an "I" piece
    if blockVal == 0:
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1":
                highestFilled = x
        toFill = highestFilled + 1
        if toFill > (MAX_HEIGHT - 4):
            sendGameOver()
        else:
            sendVal1 = ""
            for x in range(MAX_HEIGHT):
                if((x >= toFill) and x <= (toFill + 3)):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            sendPlay(play, sendVal1)
            sendVal1 = ""
    
    # Case: Block is an "O" piece
    if blockVal == 1:
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1" and x > highestFilled:
                highestFilled = x
        toFill = highestFilled + 1
        if toFill > (MAX_HEIGHT - 2):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill or x == (toFill + 1)):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            for x in range(MAX_HEIGHT):
                if(x == toFill or x == (toFill + 1)):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn1[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendVal1 = ""
            sendVal2 = ""

    # Case: Block is a "T" piece
    if blockVal == 2:
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1" and x > highestFilled:
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn2[x] == "1" and x > highestFilled:
                highestFilled = x
        toFill = highestFilled + 1
        if toFill > (MAX_HEIGHT - 2):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            for x in range(MAX_HEIGHT):
                if(x == toFill or x == (toFill + 1)):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn1[x]
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal3 = sendVal3 + "1"
                else:
                    sendVal3 = sendVal3 + playColumn2[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendPlay((play + 2), sendVal3)
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""
    
    # Case: Block is an "S" piece
    if blockVal == 3:
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1" and x > highestFilled:
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn2[x] == "1" and x > (highestFilled + 1):
                highestFilledS = x
        if((highestFilledS - highestFilled) <= 1):
            toFill = (highestFilled + 1)
        elif((highestFilledS - highestFilled) > 1):
            toFill = highestFilledS
        if toFill > (MAX_HEIGHT - 2):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            for x in range(MAX_HEIGHT):
                if(x == toFill or x == (toFill + 1)):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn1[x]
            for x in range(MAX_HEIGHT):
                if(x == (toFill + 1)):
                    sendVal3 = sendVal3 + "1"
                else:
                    sendVal3 = sendVal3 + playColumn2[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendPlay((play + 2), sendVal3)
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""

    # Case: Block is a "Z" piece
    if blockVal == 4:
        for x in range(MAX_HEIGHT):
            if playColumn2[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1" and x > highestFilled:
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1" and x > (highestFilled + 1):
                highestFilledS = x
        if((highestFilledS - highestFilled) <= 1):
            toFill = (highestFilled + 1)
        elif((highestFilledS - highestFilled) > 1):
            toFill = highestFilledS
        if toFill > (MAX_HEIGHT - 2):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal3 = sendVal3 + "1"
                else:
                    sendVal3 = sendVal3 + playColumn2[x]
            for x in range(MAX_HEIGHT):
                if(x == toFill or x == (toFill + 1)):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn1[x]
            for x in range(MAX_HEIGHT):
                if(x == (toFill + 1)):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendPlay((play + 2), sendVal3)
            sendVal1 = ""
            sendVal2 = ""
            sendVal3 = ""
    
    # Case: Block is a "J" piece
    if blockVal == 5: 
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1" and x > highestFilled:
                highestFilled = x
        toFill = highestFilled + 1
        if toFill > (MAX_HEIGHT - 3):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn0[x]
            for x in range(MAX_HEIGHT):
                if(x >= toFill and x <= (toFill + 2)):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn1[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendVal1 = ""
            sendVal2 = ""
    
    # Case: Block is an "L" piece
    if blockVal == 6:
        for x in range(MAX_HEIGHT):
            if playColumn1[x] == "1":
                highestFilled = x
        for x in range(MAX_HEIGHT):
            if playColumn0[x] == "1" and x > highestFilled:
                highestFilled = x
        toFill = highestFilled + 1
        if toFill > (MAX_HEIGHT - 3):
            sendGameOver()
        else:
            sendVal1 = ""
            sendVal2 = ""
            for x in range(MAX_HEIGHT):
                if(x == toFill):
                    sendVal2 = sendVal2 + "1"
                else:
                    sendVal2 = sendVal2 + playColumn0[x]
            for x in range(MAX_HEIGHT):
                if(x >= toFill and x <= (toFill + 2)):
                    sendVal1 = sendVal1 + "1"
                else:
                    sendVal1 = sendVal1 + playColumn1[x]
            sendPlay(play, sendVal1)
            sendPlay((play + 1), sendVal2)
            sendVal1 = ""
            sendVal2 = ""

play = ""
blockVal = 0
netrominos = ["I","O","T","S","Z","J","L"]

while True:
    blockVal = random.randint(6)

    print("[" + column0[3] + "] " + "[" + column1[3] + "] " + "[" + column2[3] + "] " + "[" + column3[3] + "] " + "[" + column4[3] + "] " + "[" + column5[3] + "] " + "[" + column6[3] + "] " + "[" + column7[3] + "] " + "[" + column8[3] + "] " + "[" + column9[3] + "] ")
    print("[" + column0[2] + "] " + "[" + column1[2] + "] " + "[" + column2[2] + "] " + "[" + column3[2] + "] " + "[" + column4[2] + "] " + "[" + column5[2] + "] " + "[" + column6[2] + "] " + "[" + column7[2] + "] " + "[" + column8[2] + "] " + "[" + column9[2] + "] ")
    print("[" + column0[1] + "] " + "[" + column1[1] + "] " + "[" + column2[1] + "] " + "[" + column3[1] + "] " + "[" + column4[1] + "] " + "[" + column5[1] + "] " + "[" + column6[1] + "] " + "[" + column7[1] + "] " + "[" + column8[1] + "] " + "[" + column9[1] + "] ")
    print("[" + column0[0] + "] " + "[" + column1[0] + "] " + "[" + column2[0] + "] " + "[" + column3[0] + "] " + "[" + column4[0] + "] " + "[" + column5[0] + "] " + "[" + column6[0] + "] " + "[" + column7[0] + "] " + "[" + column8[0] + "] " + "[" + column9[0] + "] ")

    print("Next block: " + netrominos[blockVal])
    play = int(input("Which column would you like to place the block in? \n"))
    if play == 0:
        playBlock(column0, column1, column2, blockVal, play)
    
    if play == 1:
        playBlock(column1, column2, column3, blockVal, play)
    
    if play == 2:
        playBlock(column2, column3, column4, blockVal, play)
    
    if play == 3:
        playBlock(column3, column4, column5, blockVal, play)
    
    if play == 4:
        playBlock(column4, column5, column6, blockVal, play)
    
    if play == 5:
        playBlock(column5, column6, column7, blockVal, play)
    
    if play == 6:
        playBlock(column6, column7, column8, blockVal, play)
    
    if play == 7:
        playBlock(column7, column8, column9, blockVal, play)
    
    if play == 8:
        playBlock(column8, column9, column0, blockVal, play)
    
    if play == 9:
        playBlock(column9, column0, column1, blockVal, play)
    
    getBoard()
    for x in range(MAX_HEIGHT):
        deleteRows()