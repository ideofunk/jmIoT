import mraa
import time
print(mraa.getVersion())
x = mraa.Gpio(35)
x.dir(mraa.DIR_IN)
while True:
    print("Gpio_35 state:", x.read())
    time.sleep(0.3)
#
#
#x.write(1)
