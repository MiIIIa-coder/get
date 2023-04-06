import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)

def dec2bin(value):
    return [int (elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(int(i)))
        time.sleep(0.01)
        if (1 - GPIO.input(comp) == 1):
            GPIO.output(dac, 0)
            print(i)
            return i
    return 256

try:
    while True:
        print('Voltage = %.2f' %round(adc() * 3.3 / 256, 4))
        #print('{:.4f}'.format(int(adc())*3.3/256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()