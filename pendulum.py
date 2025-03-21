from machine import Pin
import time
import neopixel
import random

#pendulum

np = neopixel.NeoPixel(Pin(4), 16)
a=0
b=15
c=0.25
np[a] = (0,0,255)
np[b] = (0,0,255)
np.write()
time.sleep(0.25)
list = [a,b]

while (a<8 and b>7):
    np[a] = (0,0,0)
    np[b] = (0,0,0)
    a=a+1
    b=b-1
    np[a] = (0,0,255)
    np[b] = (0,0,255)
    time.sleep(c)
    if (c>=0.04):
        c=c-0.04
    if (a==7 and b==8):
        np[a] = (255,0,0)
        np[b] = (255,0,0)
    if (a==8 and b==7):
        break
    print(b)
    np.write()

if (a==8 and b==7):
    while (a>2 and b<13):
        np[a] = (0,0,0)
        np[b] = (0,0,0)
        a=a-1
        b=b+1
        time.sleep(c+0.08)
        np[a] = (0,0,255)
        np[b] = (0,0,255)
        np.write()
        print(b)
        if (a==2 and b==13):
            break

time.sleep(0.15)
x=0.20

while (a<8 and b>7):
    np[a] = (0,0,0)
    np[b] = (0,0,0)
    a=a+1
    b=b-1
    np[a] = (0,0,255)
    np[b] = (0,0,255)
    time.sleep(x)
    if (x>=0.04):
        x=x-0.04
    if (a==7 and b==8):
        np[a] = (255,0,0)
        np[b] = (255,0,0)
    if (a==8 and b==7):
        break
    print(b)
    np.write()

if (a==8 and b==7):
    while (a>4 and b<11):
        np[a] = (0,0,0)
        np[b] = (0,0,0)
        a=a-1
        b=b+1
        time.sleep(x+0.08)
        np[a] = (0,0,255)
        np[b] = (0,0,255)
        print(b)
        np.write()
        if (a==4 and b==11):
            break

time.sleep(0.15)
y=0.20

while (a<8 and b>7):
    np[a] = (0,0,0)
    np[b] = (0,0,0)
    a=a+1
    b=b-1
    np[a] = (0,0,255)
    np[b] = (0,0,255)
    time.sleep(y)
    if (y>=0.08):
        y=y-0.08
    if (a==7 and b==8):
        np[a] = (255,0,0)
        np[b] = (255,0,0)
    if (a==8 and b==7):
        break
    print(b)
    np.write()

if (a==8 and b==7):
    while (a>6 and b<9):
        np[a] = (0,0,0)
        np[b] = (0,0,0)
        a=a-1
        b=b+1
        time.sleep(y+0.12)
        np[a] = (0,0,255)
        np[b] = (0,0,255)
        print(b)
        np.write()
        if (a==6 and b==9):
            break


time.sleep(0.15)
z=0.20

while (a<8 and b>7):
    np[a] = (0,0,0)
    np[b] = (0,0,0)
    a=a+1
    b=b-1
    np[a] = (0,0,255)
    np[b] = (0,0,255)
    time.sleep(z)
    if (z>=0.1):
        z=z-0.1
    if (a==7 and b==8):
        np[a] = (255,0,0)
        np[b] = (255,0,0)
    if (a==8 and b==7):
        break
    print(b)
    np.write()
