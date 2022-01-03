import socket
import time
import RPi.GPIO as GPIO

"""
Server class for a wireless network paired with Rasp_Pi_26NetworkingClient_UserInput. This program is run on the Rasberry Pi,
while the client program can be run on another computer with a wireless connection. The server receives the following valid commands and controls 
a board with 2 LEDs wirelessly (refer to circuit schematic diagram).
The valid 8-char commands are:
BOARDSET - initializes board by configuring each used GPIO pin as output and triggers value LOW
FLASHLED - flashes the LEDs until another command is called
TURNON(number) - turns on the LED at the given port (e.g.TURNON18 turns on the LED at port18)
OFFLED(number) - turns off LED at the given port (e.g.OFFLED18 turns off the LED at port 18)
BOARDOFF - triggers all output pins LOW and disables the board

Author: Katelyn Lam
Date: April 2021
"""

#defines GPIO ports of the LEDs
led1 = 11
led2 = 13

#configures LED pins to output and set to LOW. Called when BOARDSET cmd is received.
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)
    GPIO.output(led1, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)

#disables all GPIO ports after setting each output pin to LOW. Called when BOARDOFF cmd is received
def disable():
    GPIO.output(led1, GPIO.LOW)
    GPIO.cleanup()

#turns LED on at a given port (ledPin) when TURNON is received
def turnLEDOn(ledPin):
    GPIO.output(ledPin,GPIO.HIGH)

#turns LED off at a given port (ledPin) when OFFLED is received 
def turnLEDOff(ledPin):
    GPIO.output(ledPin,GPIO.LOW)

#turns on and off the LED every 1s when FLASHLED is received
def flashLED():
    GPIO.output(led1, GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sets up socket to wirelessly connect to client
HOST = "###.#.#.#" #ipaddress of the server
PORT = 65432 #data transmission port number
exitString = "BOARDOFF" #command to close socket
message = "" #command sent by the client to the server
gpioNum = 0 #accessed port number (number of port for TURNON and OFFLED commands)

#initializes socket and waits for commands from the client
s.bind((HOST,PORT))
s.listen(5)

#attempts to connect to client
print("Opening connection...")
conn, addr = s.accept()

#takes an 8-char message and converts it to a String
while (message != exitString):
    data = conn.recv(8)
    message = data.decode()

	#formats command arguments so it can be passed to action methods
    if(message[:5] == "OFFLED" or message[:5] == "TURNON"):
        message = message[:5]
		
		#converts port number to an integer. If it is less than 10, only take the value of the ones digit,
		#otherwise take the two-digit number
		if(message[len() - 2:len() - 1] == "0")
			gpioNum = int(message[:-1])
		else
			gpioNum = int(message[:-2])

	#displays message to acknowledge that command has been succesfully passed
    print("Connection established.")
    print(message)

	#executes action based on received and formatted command (see behaviour in the block comment above)
    switch(message)
    {
        case "BOARDSET":setup();
                        break
        case "FLASHLED":flashLED();
                        break
        case "OFFLED":turnLEDOff(gpioNum);
                        break
        case "TURNON":turnLEDOn(gpioNum);
                        break
        default: print("Invalid Command");
                        break
    }

#closes socket when exit command (BOARDOFF) has been passed
print("Closing connection...")
conn.close()
