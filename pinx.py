import mraa
import time
print(mraa.getVersion())
pin_num = input('Which pin? ')
pin = mraa.Gpio(pin_num)
pin.dir(mraa.DIR_IN)
while True:
    print("Gpio pin state: ", pin.read())
    time.sleep(0.3)

