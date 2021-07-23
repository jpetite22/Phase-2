import RPi.GPIO as GPIO
import blynklib
import time

BLYNK_AUTH = '7WmNA1wnN7NFTvOMm1yNm7TOywXHySUr'
blynk = blynklib.Blynk(BLYNK_AUTH)

GPIO.setmode(GPIO.BCM)

servo = 12
GPIO.setup(servo, GPIO.OUT)
ServoPWM = GPIO.PWM(servo,50)
ServoPWM.start(0)

@blynk.handle_event('write V5')
def write_virtual_pin_handler(pin, value):
    slidervalue = float(format(value[0]))
    ServoPWM.ChangeDutyCycle(SliderNumberToServoDutyCycle(slidervalue))
    time.sleep(.25)
    ServoPWM.ChangeDutyCycle(0)

# slider value to duty cycle convert equation
def SliderNumberToServoDutyCycle(value):
    return value

       
while True:
    blynk.run()