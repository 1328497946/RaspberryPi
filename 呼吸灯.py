import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
p=GPIO.PWM(18,50)
p.start(0)
try:
    while True:
        for dc in range(0, 101, 2):
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
        for dc in range(100, -1, -2):
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
