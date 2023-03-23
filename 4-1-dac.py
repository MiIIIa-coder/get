import RPi.GPIO as gpio
import sys

dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value, count):
    return [int (elem) for elem in bin(value)[2:].zfill(count)]

try:
    while(True):
        a = input('enter number ')
        if a == 'q':
            sys.exit()
        elif not a.isdigit():
            print('enter number!')
        elif int(a) < 0:
            print('enter number > 0')
        elif int(a) > 255:
            print('enter number < 256')
        else:
            gpio.output(dac, dec2bin(int(a), 8))
            print('{:.4f}'.format(int(a)*3.3/256))
except KeyboardInterrupt:
    print('stopped')

finally:
    gpio.output(dac, 0)
    gpio.cleanup() 