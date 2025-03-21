from machine import Pin
import time

c1 = Pin(12, Pin.OUT)
c2 = Pin(13, Pin.OUT)
c3 = Pin(14, Pin.OUT)
c4 = Pin(15, Pin.OUT)

seq = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]

while True:
    for i in seq:
        print (i)
        c1.value(i[0])
        time.sleep(0.001)
        c2.value(i[1])
        time.sleep(0.001)
        c3.value(i[2])
        time.sleep(0.001)
        c4.value(i[3])
        time.sleep(0.001)
