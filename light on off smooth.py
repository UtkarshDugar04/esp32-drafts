# Write your code here :-)
from machine import PWM, Pin
import time

pwm_pin = PWM(Pin(15))
pwm_pin.freq (100)

A = 1
max_duty = 1022

while True:
    while (A <= max_duty):
        pwm_pin.duty (A)
        time. sleep (0.001)
        A = A+1
        print (A)
    while A >= 1:
        pwm_pin. duty (A)
        time. sleep (0.001)
        A = A-1
        print (A)


