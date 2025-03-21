from machine import Pin,PWM

en = PWM(Pin(15))

IN1 = Pin(12,Pin.OUT)
IN2 = Pin(13,Pin.OUT)

en.freq(1000)
en.duty(1000)

def clockwise():
    IN1.value(1)
    IN2.value(0)

def anticlockwise():
    IN1.value(0)
    IN2.value(1)

while True:
    clockwise()
