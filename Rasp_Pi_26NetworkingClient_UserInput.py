import socket
import time
"""
Client class for a wireless network paired with Rasp_Pi_26NetworkingServer. Enters the following valid commands below to 
control a Raspberry Pi board with 2 LEDs wirelessly through a server, the Raspberry Pi(refer to circuit schematic diagram).

Note: The schematic diagram uses a Raspberry Pi 3B, whereas the actual program is run on a Raspberry Pi 4B

The valid 8-char commands are:
BOARDSET - initializes board by configuring each used GPIO pin as output and triggers value LOW
FLASHLED - flashes the LEDs until another command is called
TURNON(number) - turns on the LED at the given port (e.g.TURNON06 turns on the LED at port 6)
OFFLED(number) - turns off LED at the given port (e.g.OFFLED06 turns off the LED at port 6)
BOARDOFF - triggers all output pins LOW and disables the board

Author: Katelyn Lam
Date: April 2021
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a wireless socket to connect to server 

HOST = "###.#.#.#" #client's ip adress
PORT = 65432 #data transmission port num

#array of valid commands to control LEDs
command = ""

s.connect((HOST,PORT)) #connect to server

#prompts user to initialize board before calling other commands
while(command != "BOARDSET"):
    command = input("Type BOARDSET to start: ")

s.sendall(command.encode()) #sends BOARDSET command to server to initialize board

#performs other command operations and sends it to the server until BOARDOFF is called, to which board will be disabled
while(command != "BOARDOFF"):
    command = input("Enter command: ")
    s.sendall(command.encode())
    time.sleep(0.2) #set a 20 ms delay to ensure that the server receives one command at a time
	
#closes socket once the board has been disabled by the server
s.sendall(command.encode())
s.close()
