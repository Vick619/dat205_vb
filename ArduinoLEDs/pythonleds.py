import serial
import mosquitto
#establish serial port connection to arduino.
port = serial.Serial("/dev/cu.usbmodem1411",9600, timeout=2)
#run serial port script in pyserial-2.7/setup.py using terminal with :python setup.py install --user

client = mosquitto.Mosquitto("vicktor")
client.connect("141.163.83.22")
client.subscribe("lights")

def messageReceived(broker, obj, msg):
	global client
	print("Message " + msg.topic + " containing: " + msg.payload)
	#client = None
	onoff = msg.payload
	if(onoff == "ON"):
		port.write("1")
	elif(onoff == "OFF"):
		port.write("0")

client.on_message = messageReceived

while (True):
	client.loop()
####################################################################### Manual ON - OFF - through raw input

# while True:
	# input = raw_input("On or off ? ") #Input stored in input

	# if input == "on":    #If the input == "on","ON",'1' will turn LED ON.
	# 	port.write("1")
	# 	print("LED ON.")
	# elif input == "ON":
	# 	port.write("1")
	# 	print("LED ON.")
	# elif input == "1":
	# 	port.write("1")
	# 	print("LED ON.")
	# elif input == "off":#If the input == "off","OFF",'0' will turn LED OFF.
	# 	port.write("0")
	# 	print("LED OFF.")
	# elif input == "OFF":
	# 	port.write("0")
	# 	print("LED OFF.")
	# elif input == "0":
	# 	port.write("0")
	# 	print("LED OFF.")
	# elif len(input) == 0:#If nothing is written, will repspond with text.
	# 	print("Nothing was written.")
