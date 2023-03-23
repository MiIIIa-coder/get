import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)


gpio.setup(22, gpio.OUT, initial=0)
gpio.setup(21, gpio.OUT, initial=0)

p22 = gpio.PWM(22, 50)
p21 = gpio.PWM(21, 50)
p21.start(0)
p22.start(0)

try:
    while True:
        duty_cycle = input('enter Duty Cycle')
        if not duty_cycle.isdigit():
            print('enter number!')
            p21.stop()
            p22.stop()
            gpio.cleanup()
            break
        p22.ChangeDutyCycle(int(duty_cycle))
        p21.ChangeDutyCycle(int(duty_cycle))
        print('{:.4f}'.format(int(duty_cycle)*3.3/100))

except KeyboardInterrupt:
    print('stopped')

finally:
    p21.stop()
    p22.stop()
    gpio.cleanup()