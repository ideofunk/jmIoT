import mraa

print (mraa.getVersion())
x = mraa.Gpio(35)
x.dir(mraa.DIR_IN)
x.write(1)
