import RPi.GPIO as GPIO
import time
time_out = 5
infrared = 20
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(infrared, GPIO.IN)
try:
    while True:
        if GPIO.input(infrared) == True:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + " Someone is here!")
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+ "Nobody!")
        time.sleep(time_out)
except KeyboardInterrupt:
    print("done")
    GPIO.cleanup()
