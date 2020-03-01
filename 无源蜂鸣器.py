import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p=GPIO.PWM(12, 35)
p.start(0)
try:
    while 1:
        for dc in range(0, 50, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
        for dc in range(50, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
