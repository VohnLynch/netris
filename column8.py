#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 10008

columnStr = str("0000")
readStr = ""

while True:
    with open("column8.txt", "r") as readFile:
        readStr = readFile.read()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print('Connected by', addr)
        data = conn.recv(1024).decode()
        if data != columnStr and data:
            with open("column8.txt", "r+") as writeFile:
                readStr = writeFile.read()
                writeFile.seek(0)
                writeFile.write(data)
                writeFile.seek(0)
                readStr = writeFile.read()
                print(readStr)
                columnStr = data
        s.close()