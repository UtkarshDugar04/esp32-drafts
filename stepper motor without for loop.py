from machine import Pin
import time

coil1 = Pin(12, Pin.OUT)
coil2 = Pin(13, Pin.OUT)
coil3 = Pin(14, Pin.OUT)
coil4 = Pin(15, Pin.OUT)

while True:
    coil1.value(1)
    time.sleep(0.001)
    coil2.value(1)
    time.sleep(0.001)
    coil3.value(0)
    time.sleep(0.001)
    coil4.value(0)
    time.sleep(0.001)

    coil1.value(0)
    time.sleep(0.001)
    coil2.value(1)
    time.sleep(0.001)
    coil3.value(1)
    time.sleep(0.001)
    coil4.value(0)
    time.sleep(0.001)

    coil1.value(0)
    time.sleep(0.001)
    coil2.value(0)
    time.sleep(0.001)
    coil3.value(1)
    time.sleep(0.001)
    coil4.value(1)
    time.sleep(0.001)

    coil1.value(1)
    time.sleep(0.001)
    coil2.value(0)
    time.sleep(0.001)
    coil3.value(0)
    time.sleep(0.001)
    coil4.value(1)
    time.sleep(0.001)
