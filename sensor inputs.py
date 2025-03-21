from machine import Pin
import time

ldr= Pin(15)
led = Pin(14, Pin.OUT)
led.value(0)

while (True):
    u=ldr.value()
    print(u)
    if (u==1):
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.5)



