from machine import Pin, ADC
import time

adc = ADC(Pin(34))

adc.atten(ADC.ATTN_11DB)

while True:
    adc_value = adc.read()
    print("ADC Level:", adc_value)
    time.sleep(0.1)
