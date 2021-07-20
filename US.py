import blynklib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 18
GPIO_ECHO = 24

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

BLYNK_AUTH = 'W68HtGwXXdUx9UNH9tk_37sig8llw8Ni'
blynk = blynklib.Blynk(BLYNK_AUTH)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"

@blynk.handle_event('read V11')
def read_virtual_pin_handler(pin):
    blynk.virtual_write(pin,distance())

def distance():
    GPIO.output(GPIO_TRIG,True)
    
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    while GPIO.input(GPIO_ECHO) ==0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
    TimeElapsed = StopTime - StartTime
    distance = TimeElapsed*34300/2
    
    return distance

while True:
    blynk.run()
