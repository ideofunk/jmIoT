import mraa
import time
i = 100 # start with LED 100
while True:
    board_LED = mraa.Gpio(i) # access LEDs with mraa library
    board_LED.dir(mraa.DIR_OUT)
    i = i + 1 # cycle through LEDs
    board_LED.write(1)
    time.sleep(1)
    board_LED.write(0)
    time.sleep(1)
    del board_LED # delete the LED we're on to move onto the next one
#    print(i)
    if i >= 105:
        i = 100 # once LED 105 is reached, start over
 
