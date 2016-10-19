import mraa
import time
i = 100
while True:
    board_LED = mraa.Gpio(i) #onboard LED
    board_LED.dir(mraa.DIR_OUT)
    i = i + 1
    board_LED.write(1)
    time.sleep(1)
    board_LED.write(0)
    time.sleep(1)
    delete
#    print(i)
    if i >= 105:
        i = 100
 
