import board
import busio
import time


import adafruit_sgp40
from adafruit_bme280 import basic as adafruit_bme280
import in13


i2c = busio.I2C(board.GP17, board.GP16)
sgp = adafruit_sgp40.SGP40(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
# Initialize IN13 driver
indicator = in13.IN13(i2c, addr = 0x13)
indicator.filter = 1.0
indicator.value = 1.0
time.sleep(1)
indicator.value = 0
time.sleep(1)
indicator.value = 1.0
time.sleep(1)
indicator.value = 0
time.sleep(1)
indicator.value = 1.0
time.sleep(1)

while True:
    print("Raw Gas: ", sgp.raw)
    # Lets quickly grab the humidity and temperature
    temperature = bme280.temperature
    humidity = bme280.relative_humidity
    compensated_raw_gas = sgp.measure_raw(temperature = temperature, relative_humidity = humidity)
    print(f"compensated raw gas: {compensated_raw_gas}")
    
    # For Compensated voc index readings
    voc_index = sgp.measure_index(temperature=temperature, relative_humidity=humidity)
    print(f"VOC index: {voc_index}")
    
    if (voc_index == 0):
        value = 0
    else:
        value = voc_index/500
    print(f"Indicator value: {value}")
    indicator.value = value
    print("")
    time.sleep(1)