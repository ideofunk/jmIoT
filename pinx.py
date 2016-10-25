import mraa
import time
print(mraa.getVersion())

pin_num = input('Which pin? ') #so I can test different pins with this same file
pin = mraa.Gpio(pin_num)
pin.dir(mraa.DIR_IN)
while True:
    print('Pin ', pin_num, ' is: ', pin.read())
    time.sleep(0.3)

