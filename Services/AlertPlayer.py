import time
from Constants.GpioAddress import BUZZER_GPIO
import RPi.GPIO as GPIO



class alertPlayer:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)  # use BCM numbers
        GPIO.setup(BUZZER_GPIO, GPIO.OUT)  # set pin OUTPUT mode
        global Buzz                     # Assign a global variable to replace GPIO.PWM
        Buzz = GPIO.PWM(BUZZER_GPIO, 440) # 440 is initial frequency.
    
    def play(self):
        Buzz.start(50) 
        time.sleep(1)  # wait for 1 ms
        Buzz.start(0) 
        
            
