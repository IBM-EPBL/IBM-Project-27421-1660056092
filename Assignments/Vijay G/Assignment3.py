import time
import RPi.GPIO as GPIO
from gpiozero import Button, TrafficLights, Buzzer
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)
    time.sleep(1)
buzzer =Buzzer(15)
button =Button(21)
lights =TrafficLights(24, 7, 6) 
while True:  
    button.wait_for_press()
    light.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()

   
    buzzer.on()
    sleep(1)
    buzzer.off() 