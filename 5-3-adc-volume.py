import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)

def dec2bin(value):
    return [int (elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    left  = 0
    right = 255
    while (right - left > 1):
        middle = (right+left)//2
        GPIO.output(dac, dec2bin(middle))
        time.sleep(0.1)
        if 1 - GPIO.input(comp):
            right = middle
        else:
            left = middle
    print(left)
    return left


try:
    while True:
        print('Voltage = %.2f' %round(adc() * 3.3 / 256, 4))
        #print(bin(adc())[2:].zfill(8))
        GPIO.output(leds, dec2bin(adc()))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()