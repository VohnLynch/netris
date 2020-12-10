#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 10000

columnStr = str("0000")
readStr = ""

run = True

while run:
    with open("column0.txt", "r") as readFile:
        readStr = readFile.read()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024).decode()
        if data == "END":
            s.close()
            readFile.close()
            with open("column0.txt", "r+") as writeFile:
                readStr = writeFile.read()
                writeFile.seek(0)
                writeFile.write("0000")
                columnStr = data
                writeFile.close()
            run = False
        if data != columnStr and data and data != "END":
            with open("column0.txt", "r+") as writeFile:
                readStr = writeFile.read()
                writeFile.seek(0)
                writeFile.write(data)
                writeFile.seek(0)
                readStr = writeFile.read()
                columnStr = data
                writeFile.close()