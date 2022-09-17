import time
from Constants.GpioAddress import BUZZER_GPIO
import RPi.GPIO as GPIO



class alertPlayer:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # use BCM numbers
        GPIO.setup(BUZZER_GPIO, GPIO.OUT)  # set pin OUTPUT mode
    
    def play(self):
        
            GPIO.output(BUZZER_GPIO, GPIO.HIGH)
            time.sleep(1)  # wait for 1 ms
            GPIO.output(BUZZER_GPIO, GPIO.LOW)
            
