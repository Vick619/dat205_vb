import serial
#establish serial port connection to arduino.
port = serial.Serial("/dev/cu.usbmodem1411",9600, timeout=2)
#######################################################################

while True:
	input = raw_input("On or off ? ") #Input stored in input

	if input == "on":    #If the input == "on","ON",'1' will turn LED ON.
		port.write("1")
		print("LED ON.")
	elif input == "ON":
		port.write("1")
		print("LED ON.")
	elif input == "1":
		port.write("1")
		print("LED ON.")
	elif input == "off":#If the input == "off","OFF",'0' will turn LED OFF.
		port.write("0")
		print("LED OFF.")
	elif input == "OFF":
		port.write("0")
		print("LED OFF.")
	elif input == "0":
		port.write("0")
		print("LED OFF.")
	elif len(input) == 0:#If nothing is written, will repspond with text.
		print("Nothing was written.")
