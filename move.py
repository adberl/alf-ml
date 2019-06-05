import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 21
GPIO_ECHO = 20

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

outpin_list = [18, 24, 25, 12]
GPIO.setup(outpin_list, GPIO.OUT)

sensors = [4, 17, 27, 22, 13, 26]
GPIO.setup(sensors, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def stop():
	GPIO.output([12, 18, 24, 25], GPIO.LOW)

def rot_left(timef):	
	GPIO.output([18, 25, 12], GPIO.LOW)
	GPIO.output(12, GPIO.HIGH)
	time.sleep(timef)
	stop()

def rot_right(timef):	
	GPIO.output([18, 25, 12], GPIO.LOW)
	GPIO.output(24, GPIO.HIGH)
	time.sleep(timef)
	stop()

def go_forwards(timef):
	GPIO.output([12, 24], GPIO.HIGH)
	GPIO.output([18, 25], GPIO.LOW)		
	time.sleep(timef)
	stop()
	
def go_backwards(timef):
	GPIO.output([12, 24], GPIO.LOW)
	GPIO.output([18, 25], GPIO.HIGH)		
	time.sleep(timef)
	stop()
	
def distance():
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	print("Distance to nearest object: %0.1fcm" % distance)
	
def sensors_output():
	
	inputArray = []
	for i in sensors:
		inputArray.append(GPIO.input(i))
	print(inputArray)
	
while True:
	cmd = input('Input command and optional argument\n')
	cmd = cmd.split(' ')

	if(len(cmd) == 1):
		cmd.append(1)
	else:
		cmd[1] = float(cmd[1])
	if(cmd[0] == 'h'):
		print('f <t>\tmove forwards for t seconds')
		print('b <t>\tmove backwards for t seconds')
		print('rr <t>\trotate right for t seconds')
		print('rl <t>\trotate left for t seconds')
		print('s <t>\tstop all movement')
		print('d\tget distance to nearest object')
		print('l\tget front sensors output')
		print('h\tshow this help page')
		print('e\tend program')
		
	elif(cmd[0] == 'f'):
		go_forwards(cmd[1])
	elif(cmd[0] == 'b'):
		go_backwards(cmd[1])
	elif(cmd[0] == 'rr'):
		rot_right(cmd[1])
	elif(cmd[0] == 'rl'):
		rot_left(cmd[1])
	elif(cmd[0] == 's'):
		stop()
	elif(cmd[0] == 'd'):
		distance()
	elif(cmd[0] == 'l'):
		sensors_output()
	elif(cmd[0] == 'e'):
		GPIO.cleanup()
		break

print('done')
