# Raspberry-Pi---Networking
Allows a remote device (the client) to wirelessly control the behaviour of two LEDs on a Raspberry Pi (the server). The client can turn the LEDs on and off, or to flash together.
Run the server program on the Raspberry Pi, using the Pi's IP address. Run the client on another device and record that IP address, or use the loopback address of the Raspberry Pi. Both the client program and the server program must be run at the same time.

The user interacts with the program on the client to control the LEDs through a console when the program is run.
The following commands are valid (case-sensitive, no spaces):

BOARDSET - initializes board by configuring each used GPIO pin as output, LEDs are initially off
FLASHLED - flashes the LEDs simultaneously
TURNON(number) - turns on the LED at the given port (e.g.TURNON18 turns on the LED at port18)
OFFLED(number) - turns off LED at the given port (e.g.OFFLED18 turns off the LED at port 18)
BOARDOFF - turns all LEDs off, disables board

Refer to "Schematic_Networking.pdf" for the schematic diagram of the LED circuit. The program was tested on a Raspberry Pi 4B and uses the RPi.GPIO library.
