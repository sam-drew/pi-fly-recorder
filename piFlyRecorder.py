#!/usr/bin/env python

import time
from bmp280 import BMP280
from icm20948 import ICM20948

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

interval = (1/20)

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

baseline_values = []
baseline_size = 100

print("Collecting baseline values for {:d} seconds. Do not move the sensor!\n".format(baseline_size))

for i in range(baseline_size):
    pressure = bmp280.get_pressure()
    baseline_values.append(pressure)
    time.sleep(1)

baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])

imu = ICM20948()

counter = 0
logCounter = 0

data = []

while True:
    counter += 1
    x, y, z = imu.read_magnetometer_data()
    ax, ay, az, gx, gy, gz = imu.read_accelerometer_gyro_data()
    altitude = bmp280.get_altitude(qnh=baseline)
    data.append({
        "mx": x,
        "my": y,
        "mz": z,
        "ax": ax,
        "ay": ay,
        "az": az,
        "gx": gx,
        "gy": gy,
        "gz": gz,
        "alt": altitude

    })
    if counter == 1000:
        # Reset counter
        counter = 0
        # Update log counter
        logCounter += 1
        # Output data to file
        with open(("pifly-log-" + logCounter + ".json"), "w") as write_file:
            json.dump(data, write_file)

    time.sleep(interval)
