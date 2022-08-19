import time
from Constants.GpioAddresses import BUZZER_GPIO
import RPi.GPIO as GPIO


def play():
    
    i1 = 0

i2 = 0
GPIO.setmode(GPIO.BCM)  # use BCM numbers
GPIO.setup(BUZZER_GPIO, GPIO.OUT)  # set pin OUTPUT mode

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

GPIO.cleanup()  # release all GPIO