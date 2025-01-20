# IN13 Nixie Tube VOC Indicator
A VOC air quality monitor using an SGP40, BME280 and an IN13 nixie bar graph tube as the VOC level indicator.

The primary reason for this project was I have a small, fairly crowded office where I make stuff and also do my day job. I frequently need to keep my door closed while on phone calls to avoid annoying the rest of the family that is also doing work and school from home. I also frequently start 3D print jobs to get parts rolling while working, so I wanted something to check VOC levels and give me a visual indicator as to when it might be a good idea to open my door or a window. Also, I had a really cool IN13 nixie bargraph tube with driver board that I wanted to try...

![Warm photo of an IN13 Nixie tube inside a glass test tube, mounted on a warm wood grain 3D printed case. In the backround of the photo is a skull shaped bottle full of unlit LEDs, part of a lamp, a picture frame and a power supply](/media/IMG_4198.jpg)

## Hardware I used and where I got it:
- IN13 bargraph nixie tube with driver board from *eclipsevl* on Tindie, available here: https://www.tindie.com/products/eclipsevl/in-13-bargraph-nixie-tube-with-driver-and-dc-dc/
- Adafruit SGP40 VOC Air quality sensor, available here: https://www.adafruit.com/product/4829
- Adafruit BME280 temperature, humidity and pressure sensor, available here: https://www.adafruit.com/product/2652
- Raspberry Pi Pico 2 W as the microcontroller, available here: https://www.adafruit.com/product/6087
- 20mm 3.3v fan, available here (but probably elsewhere too): https://www.amazon.com/Easycargo-2pcs-20mm-Small-Quite/dp/B0CFKYVVXL
- 30mm OD x 165mm glass test tube, https://www.amazon.com/dp/B07Z5YM4SN
- 2 x M2 10mm bolts and M2 nuts
- 2 x JST-SH to female dupont cable: https://www.adafruit.com/product/4397
- 1 x 50mm JST-SH (or QT) cable: https://www.adafruit.com/product/4399

## Tools
- 3D printer, I'm using an Ender 5s1 (I'm continually tempted to get a better printer, but this one works fine so resisting so far)
- wire stripper
- soldering iron
- screw driver or socket driver for the M2 bolts if using the fan
- (optional) hot glue gun, I love my Hoto.

## 3D Printed case:
The 3 piece case is availabe in the [stl folder](/stl/). The three pieces are:
- [Nixie case bottom.stl](/stl/Nixie%20case%20bottom.stl), bottom piece with mounting posts for the Pico, SGP40, BME280 and a small 20mm 3.3v fan. These mounts aren't the strongest, so careful.
- [Nixie case top.stl](/stl/Nixie%20case%20top.stl), the top of the case with hole for the IN13 and a circular slot for a glass test tube to provice a bit of protection for the nixie tube.
- [Nixie case round top.stl](/stl/Nixie%20case%20round%20top.stl), a rounded top to give the case a bit nicer feel while also helping to hold the test tube straighter. This can be glued to the case top piece or just rest on top.

![Rendering of the round bottom part of case, in red on a white background, the part is casting a shadow to the left and mounting posts and vent holes are visible](/media/t725.png)

The case has places to mount/place an optional small 20mm 3.3v fan (like this [one from Amazon](https://www.amazon.com/Easycargo-2pcs-20mm-Small-Quite/dp/B0CFKYVVXL)) and a 30mm by 165mm glass test tube (also available at [Amazon](https://www.amazon.com/dp/B07Z5YM4SN?th=1) among other places). The fan was added to make sure there was some airflow through the case for the VOC sensor.

I printed first with [Amolen Rainbow Wood PLA](https://www.amolen.com/products/pla-wood?_pos=1&_fid=7d004695e&_ss=c) filament. I got this printing the above stl's pretty well with PrusaSlicer (on an Ender 5s1), but the slow filament color change in this mostly just resulted in my smaller parts having oddly differing colors. I switched to the Amolen Wood Grain PLA which I'd previously used for [another project](https://github.com/avnc/co2_gauge). The printing characteristics of this one differ a bit (I think they have different wood content percentages) and this resulted in some stringiness and impreciseness, but this was mostly on the interior of the bottom piece and easy to cleanup with a razer. Some additional cleanup is probably needed with the IN13 mount hole and the test tube slot. Making these bigger resulted in those pieces being too loose, but too tight and they crack while trying to get them in place. I lost one of my two IN13 tubes this way (they have some variance in OD so what was perfect for one was not for the other). Also a couple of test tubes didn't survive, these are very thin so it takes very little stress to crack them.

# Assembly
I won't go into too much detail here, it is pretty straightforward. I'll assume you know your way around the Pico's pins, soldering, etc as a starting point. If you don't, you might want to be extra careful and/or use a breadboard to prototype (I did!).
1. Cut the female connectors off one of the JST-SH QT to female socket cables, and then use a wire stripper to prepare these for soldering to the Pico.
2. Cut the connectors from the 20mm fan wires (if using), and also prep them for soldering.
3. You have a couple of options here as to wiring (the Pico offers a lot of flexibility), just be sure to solder or otherwise connect the red to power output and black to ground. I used VSYS which generates a 3.3V output, though this was accidental (I'd intended to use VBUS originally for the IN13 as it should have a 5V input but turns out it runs fine on 3.3V too), the blue wire should go to an I2C SDA pin and the yellow to an SCL pin on same I2C bus (I used GP17 and GP16 for this)
3. The red wire from fan should go to another power pin (I used 3V3(OUT) for this) and the black from the fan to any ground pin.
4. Connect the other JST-SH to female dupont connector to the IN13 driver board (using the female connectors). Red to power, black to ground, blue to SDA and yellow/orange to SCL.
5. Connect the other end of the same cable (with the 4 pin JST-SH connector) to either of the Adafruit boards.
6. Connect the two Adafruit boards via the 50mm JST-SH cables.
7. Connect the JST-SH cable that was soldered to the Pico to the other Adafruit board (with the remaining open JST-SH connector)
8. Connect a USB cable from computer to Pico and copy the CircuitPython firmware (if not already done), the libraries from Adafruit and the `IN13.py` driver to lib, and then the `code.py` to the root of the CIRCUITPY drive (that should appear when the device is connected after the firmware has been loaded).

# Software
I went with CircuitPython to be able to use the nice existing driver libraries available for the two sensor boards from Adafruit. The CircuitPython firmware for the Raspberry Pi Pico 2W can be found at the [CircuiPython.org download site](https://circuitpython.org/downloads). The Adafruit drivers are both available in the [CircuitPython library bundle](https://circuitpython.org/libraries).

There is a nice driver available for the IN13 in the repo from *BrianPugh* here: https://github.com/BrianPugh/micropython-libs/blob/main/lib/in13.py. As I chose to go with CircuitPython rather than Micropython, I had to make some small modifications to the driver to get it working. This was a simple change and required small changes to use the CircuitPython I2CDevice class instead of the Micropython i2c class. The converted CircuitPython version of Brian's driver is the the [in13.py](/lib/in13.py) file in the lib folder.

When you have everything in your controllers lib directory, you should have the following (the Adafruit drivers each have a folder that should be copied in their entirety).
- /adafruit_bme280
- /adafruit_bus_device
- /adafruit_sgp40
- in13.py

With the provided libraries for the IN13, SGP40 and BME280, the rest of the code is relatively simple. To instantiate the i2c bus and the attached devices we do:
```python
i2c = busio.I2C(board.GP17, board.GP16)
# devices
sgp = adafruit_sgp40.SGP40(i2c)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
indicator = in13.IN13(i2c, addr = 0x13)
```
We then set up the nixie tube driver filter, which controls the speed of the change of values. Setting this slower or not doesn't matter much for our use case (as our values mostly change slowly) but we set it to the slowest level anyway. Following this, we run a quick test on the tube, setting it to it's highest level and then down to 0.
```python
# set filter for IN13, controls how fast the indicator changes (1.0 being the slowest)
indicator.filter = 1.0
# quick test that IN13 is working by setting to max and min values
indicator.value = 1.0
time.sleep(1)
indicator.value = 0
...
```
Finally we have our main loop which will first grab the temperature and humidity from the BMP280 sensor and then feed those values into the SGP40 measure_index function to give us a compensated (by our local environment) VOC index. This is a value the sensor calculates from the raw gas values that is on a 0-500 scale. We then simply convert this to the 0.0 to 1.0 value that is needed for the IN13 and set it.

```python
# our main loop to read the sensor data and set the IN13 value
while True:
    print("Raw Gas: ", sgp.raw)
    # Lets grab the humidity and temperature
    temperature = bme280.temperature
    humidity = bme280.relative_humidity
    
    # For Compensated voc index readings
    voc_index = sgp.measure_index(temperature=temperature, relative_humidity=humidity)
    print(f"VOC index: {voc_index}")
    
    # convert voc index to a value from 0 to 1.0 for the IN13 tube
    if (voc_index == 0):
        value = 0
    else:
        value = voc_index/500
        
    print(f"Indicator value: {value}")
    indicator.value = value
```

## Future changes
I've got another IN13 on order to make another one of these and have a few changes on deck for that one:
- Report the metrics via a Prometheus endpoint so I can collect the VOC data over time (and make use of the wireless capabilities of the RPi Pico 2 W).
- Look for a better glass cover, not sure I like the look of the tubes (and they are fragile for sure). Maybe one without a lip would work better.
- Make a better mount for the fan, this needs a bit more strength and also could possibly be positioned a little better (it's tight to get the nuts in there to secure it). I may need to change the dimensions of the case to make this a little easier to fit also.
- Make the board mounts snap-fits instead of the post and hole mounting. The posts seem to be good for only one mounting, and snap off easily if you have to take the board off. Could be other filaments would be stronger here.