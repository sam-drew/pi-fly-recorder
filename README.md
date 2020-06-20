# Pi Fly Recorder
Turn a Raspberry Pi into a flight recorder with gyros/accel/altitude. Could be useful for developing model rockets, drones, and other flying things.

Logs accelerometer, gyroscope, magnetic field (compass) readings in 3 axes, altitude info is calculated using atmospheric pressure. By default logs at about 20Hz.

This is not designed to be used as a flight computer, you should probably build something from the ground up for that. Check out [bps.space](https://bps.space), they make some cool stuff.

### Hardware
The hardware this is tested on uses:
- A Raspberry Pi 4
- Pimoroni's [ICM20948 Breakout Board](https://shop.pimoroni.com/products/icm20948)
- Pimoroni's [BMP280 Breakout Board](https://shop.pimoroni.com/products/bmp280-breakout-temperature-pressure-altitude-sensor)

### How to use
Set up the hardware, an easy way to do this would be to use Pimoroni's [breakout garden](https://pimoroni.com/breakouts).

Make sure you switch on I2C on the Pi, by running:
```
$ raspi-config
```
and select Interfacing Options, and enable I2C.

Install dependencies:
```
$ sudo pip3 install icm20948 bmp280
```

Run the script!
```
$ python3 piFlyRecorder.py
```

The altitude sensor will need to calibrate for 100 seconds before data logging will begin. *DO NOT* move the sensor whilst calibration is happening.

### Output
Data will be written out to JSON format log files every 1000 cycles. Files will be named `pifly-log-x.json` where `x` is the cycle number.

Log files look similar to this:

```
// TODO
```
