import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
import adafruit_bno055
import board
import time
import numpy as np
import matplotlib.pyplot as plt
import wave


i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)


fig = plt.figure(figsize=(6, 3))
x = [0]
yx = [0]
yy = [0]
yz = [0]
data = []

lnx, = plt.plot(x, yx, '-')
lny, = plt.plot(x, yy, '-')
lnz, = plt.plot(x, yz, '-')
plt.axis([0, 100, -10, 10])
i = 0

def update(frame):
    global i
    i += 1

    """ getting sensor data and printing immediately"""
    print(sensor.temperature)
    print(sensor.euler)
    print(sensor.gravity)
    data.append(sensor.gravity)
    print()

    x.append(i)
    yx.append(sensor.gravity[0])
    yy.append(sensor.gravity[1])
    yz.append(sensor.gravity[2])
    lnx.set_data(x, yx) 
    lny.set_data(x, yy) 
    lnz.set_data(x, yz) 

    if i > 90:
        plt.axis([(i-90), 100+(i-90), -10, 10])

    print("list",lnx)

    return lnx,lny,lnz

animation = FuncAnimation(fig, update, interval=50)
plt.show()
