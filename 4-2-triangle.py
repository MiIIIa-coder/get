import RPi.GPIO as gpio
import sys
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value, count):
    return [int (elem) for elem in bin(value)[2:].zfill(count)]

try:
    while(True):
        t = input('enter time ')
        if t == 'q':
            sys.exit()
        elif not t.isdigit():
            print('enter number!')

        else:
            time_sleep = int(t)/256/2
            for i in range(256):
                gpio.output(dac, dec2bin(i, 8))
                time.sleep(time_sleep)
            for i in range(255,-1,-1):
                gpio.output(dac, dec2bin(i, 8))
                time.sleep(time_sleep)
except KeyboardInterrupt:
    print('stopped')

finally:
    gpio.output(dac, 1)
    gpio.cleanup()