#Libraries
import RPi.GPIO as GPIO
from time import sleep
#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and Buzzer pins
Button = 22
#beyaz
Buzzer = 17
#mor
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(Buzzer,GPIO.OUT)
#Run forever loop
while True:
    button_state = GPIO.input(Button)
    if button_state == 0:
        GPIO.output(Buzzer,GPIO.LOW)
        sleep(0.5)
    else:
        GPIO.output(Buzzer,GPIO.HIGH)
        sleep(0.5) # Delay in seconds
