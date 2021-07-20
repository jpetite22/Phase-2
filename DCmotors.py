import RPi.GPIO as GPIO
import blynklib

BLYNK_AUTH = '7WmNA1wnN7NFTvOMm1yNm7TOywXHySUr'

blynk = blynklib.Blynk(BLYNK_AUTH)

motorR1 = 19
motorR2 = 26
motorL1 = 20
motorL2 = 21

motorState = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorR1,GPIO.OUT)
GPIO.setup(motorR2,GPIO.OUT)
GPIO.setup(motorL1,GPIO.OUT)
GPIO.setup(motorL2,GPIO.OUT)

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    switch = (format(value[0]))
    if switch == "0":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 0)
    elif switch == "1":
        GPIO.output(motorR1, 1)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 1)
        GPIO.output(motorL2, 0)

@blynk.handle_event('write V2')
def write_virtual_pin_handler(pin, value):
    motorReverse = (format(value[0]))
    if  motorReverse == "1":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 1)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 1)
        
    elif motorReverse == "0":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 0)
        
@blynk.handle_event('write V3')
def write_virtual_pin_handler(pin, value):
    motorLeft = (format(value[0]))
    if  motorLeft == "1":
        GPIO.output(motorR1, 1)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 1)
        
    elif motorLeft == "0":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 0)
        
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    motorRight = (format(value[0]))
    if  motorRight == "1":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 1)
        GPIO.output(motorL1, 1)
        GPIO.output(motorL2, 0)
        
    elif motorRight == "0":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 0)
        
while True:
    blynk.run()
