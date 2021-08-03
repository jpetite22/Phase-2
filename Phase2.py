import RPi.GPIO as GPIO
import blynklib
import time

BLYNK_AUTH = '7WmNA1wnN7NFTvOMm1yNm7TOywXHySUr'

# initialize blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

motorR1 = 19
motorR2 = 26
motorL1 = 20
motorL2 = 21
trig = 18
echo = 24

motorState = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorR1,GPIO.OUT)
GPIO.setup(motorR2,GPIO.OUT)
GPIO.setup(motorL1,GPIO.OUT)
GPIO.setup(motorL2,GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"

@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin,distance())

def distance():
    #set Trigger to HIGH
    GPIO.output(trig,True)
    
    #set Trigger after .01 ms to LOW
    time.sleep(0.0001)
    GPIO.output(trig, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(echo) ==0:
        StartTime = time.time()
        
    while GPIO.input(echo) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = TimeElapsed*34300/2
    
    return distance

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    motorForward = (format(value[0]))
    if motorForward == "0":
        GPIO.output(motorR1, 0)
        GPIO.output(motorR2, 0)
        GPIO.output(motorL1, 0)
        GPIO.output(motorL2, 0)
    elif motorForward == "1":
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
