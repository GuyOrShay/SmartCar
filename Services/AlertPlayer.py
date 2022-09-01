import time
from Constants.GpioAddress import BUZZER_GPIO
import RPi.GPIO as GPIO



class alertPlayer:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # use BCM numbers
        GPIO.setup(BUZZER_GPIO, GPIO.OUT)  # set pin OUTPUT mode
    
    def play(self):
        i1 = 0
        i2 = 0

        while (i1 < 50):
            GPIO.output(BUZZER_GPIO, GPIO.HIGH)
            time.sleep(0.001)  # wait for 1 ms
            GPIO.output(BUZZER_GPIO, GPIO.LOW)
            time.sleep(0.001)
            i1 = i1 + 1
            time.sleep(0.3)
        while (i2 < 50):
            GPIO.output(BUZZER_GPIO, GPIO.HIGH)
            time.sleep(0.001)  # wait for 1 ms
            GPIO.output(BUZZER_GPIO, GPIO.LOW)
            time.sleep(0.001)
            i2 = i2 + 1
            time.sleep(1)
