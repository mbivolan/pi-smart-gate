from evdev import InputDevice, categorize, ecodes

def rfid_read():
	dev = InputDevice('/dev/input/event1')
	keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

	rfid_code = ""
	for event in dev.read_loop():
		if event.type==1 and event.value==1:
			if event.code==28:
				print("Code '%s'" % (rfid_code))
				rfid_code = ""
			else:
				rfid_code += keys[event.code]

if __name__ == '__main__':
	rfid_read()
