import mraa
import time

while True:
    for i in range(5):
     x = mraa.Gpio("10" + i) #onboard LED
     x.dir(mraa.DIR_OUT)
     x.write(1)
     time.sleep(1)
     x.write(0)
     time.sleep(1)
     i + 1