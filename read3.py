#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 10013

readStr = ""
run = True

while run:
    with open("column3.txt", "r") as readFile:
        readStr = readFile.read()
        readFile.seek(0)
        readFile.close()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024).decode()
        if data == "GET":
            with open("column3.txt", "r") as readFile:
                readStr = readFile.read()
                readFile.seek(0)
                readFile.close()
                conn.sendall(readStr.encode())
        if data == "END":
            s.close()
            run = False