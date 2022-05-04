import RPi.GPIO
from time import sleep

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(12, RPi.GPIO.OUT)

pig = RPi.GPIO.PWM(12, 50)
pig.start(7.25)

counter = 0
while (counter < 3):
    pig.ChangeDutyCycle(2.5)
    sleep(1)
    pig.ChangeDutyCycle(7.25)
    sleep(1)
    pig.ChangeDutyCycle(12)
    sleep(1)
    pig.ChangeDutyCycle(7.25)
    sleep(1)
    counter = counter + 1

pig.stop()
RPi.GPIO.cleanup()