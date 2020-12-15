# Netris
A simple version of Tetris spread across nodes in a network

## General Information
This program simulates a rudimentary version of the video game Tetris, but with the added functionality of storage across several files. Each of these files, when the program is running, can only be accessed through read/write functions in the main file.

## How to play
By running the application with the command ```python netrisMain.py```, the game will begin. The user will be prompted with a simple output displaying the current block configuration of the 10-by-10 board (empty). The user will also be prompted with the next block to be played and asked to choose the position that they would like to place this block (position denotes left-most block placement). Blocks can wrap around the field horizontally. Upon placement of a block that would exceed the bounds of the game vertically, the application will stop and deliver a game over message.

## Code information
This application runs on Python, utilizing the socket, threading, and subprocess libraries for server-client functionality. The main gameplay loop involves pulling data from the "remote" column storage files, storing these values in lists locally, printing these values to the user, then sending user prompts to the servers.

Gameplay loops infinitely, or until the application receives placement which would extend beyond the 10 block height limit. Upon this command being received, all servers are notified of the game over and clear the contents of their respective column files.

## Testing
Code testing was performed with the unittest python library, using assertions to test that the input of each value from the user correlated with the correct storage command. This concerns both the storage of data in the column files as well as the data within the local lists which are pulled from said files.