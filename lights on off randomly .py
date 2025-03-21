from machine import Pin
import time
import neopixel
import random

np = neopixel.NeoPixel(Pin(21), 16)
list = []
listtwo = []
num = 1

while True:
        while (num<17):
            num=num+1
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            x = random.randint(0,15)
            while x in list:
                x = random.randint(0,15)
            list.append(x)
            print(list)
            np[x] = (a,b,c)
            np.write()
            time.sleep(0.1)
        if (num==17):
            while (num>1):
                num = num-1
                x = random.randint(0,15)
                while x in listtwo:
                    x = random.randint(0,15)
                listtwo.append(x)
                print(listtwo)
                np[x] = (0,0,0)
                np.write()
                time.sleep(0.1)
            list.clear()
            listtwo.clear()
