import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
#GPIO.setup(troyka, GPIO.OUT, initial=1)

def dec2bin(value):
    return [int (elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    left  = 0
    right = 255
    while (right - left > 1):
        middle = (right+left)//2
        GPIO.output(dac, dec2bin(middle))
        time.sleep(0.0005)
        if 1 - GPIO.input(comp):
            right = middle
        else:
            left = middle
    #print(left)
    return left

try:
    results = []
    value = 0
    count = 0
    time_start = time.time()

    #зарядка
    while value <= 256*0.8:
        value = adc()
        print(value)
        results.append(value)
        #time.sleep(0.001)
        count += 1
        GPIO.output(leds, dec2bin(value))
    value_max = value

    GPIO.setup(troyka, GPIO.OUT, initial=1)
    print('__________')
    #разрядка
    while value > 256*0.3:
        value = adc()
        print('F', value)
        results.append(value)
        #time.sleep(0.001)
        count += 1
        GPIO.output(leds, dec2bin(value))
    value_min = value

    time_end = time.time()
    time_exp = time_end - time_start

    #запись в файл
    with open('data.txt', 'w') as f:
        f.seek(0)
        for i in results:
            f.write(str(i) + '\n')
        
    with open('settings.txt', 'w') as f:
        f.seek(0)
        f.write(str(1/time_exp/count) + '\n')
        f.write(str(3.3/256))

    print('Общая продолжительность эксперимента', time_exp)
    print('Период одного измерения', time_exp/count)
    print('Средняя частота дискретизации', 1/time_exp/count)
    print('Шаг квантования АЦП', 3.3/256)

    #график
    y = [i*3.3/256 for i in results]
    x = [i*time_exp/count for i in range(len(results))]
    pyplot.title('U(t) graphik')
    pyplot.plot(x,y)
    pyplot.xlabel('время')
    pyplot.ylabel('напряжение')
    pyplot.show()
finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()

