from machine import Pin
import time

c1 = Pin(12, Pin.OUT)
c2 = Pin(13, Pin.OUT)
c3 = Pin(14, Pin.OUT)
c4 = Pin(15, Pin.OUT)

seq = [[1,1,0,0], [0,1,1,0], [0,0,1,1], [1,0,0,1]]
coil = [c1,c2,c3,c4]


while True:
    for i in seq:
        n=0
        for n in range(0,4,1):
            print(coil[n])
            print(i)
            coil[n].value(i[n])
            time.sleep(0.001)
