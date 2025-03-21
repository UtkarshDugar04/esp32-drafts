from machine import Pin, TouchPad
import time

TestWire = TouchPad(Pin(4))
Red = Pin(13, Pin.OUT) #distilled
Blue = Pin(12, Pin.OUT) #salt
Yellow = Pin(14, Pin.OUT) #sugar
#Green = Pin(27, Pin.OUT) #soap
Buzzer = Pin (5, Pin.OUT)

Buzzer.value(0)

while True:
    Cap = TestWire.read()
    print(Cap)
    time.sleep(0.5)

    if (430<Cap<500):
        Blue.value(1)
        Buzzer.value(1)
        time.sleep(1)
        Buzzer.value(0)
        Blue.value(0)

    if (350<Cap<430):
        Red.value(1)
        Buzzer.value(1)
        time.sleep(1)
        Buzzer.value(0)
        Red.value(0)

    if (200<Cap<350):
        Yellow.value(1)
        Buzzer.value(1)
        time.sleep(1)
        Buzzer.value(0)
        Yellow.value(0)




