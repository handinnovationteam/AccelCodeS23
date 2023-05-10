import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randrange
import adafruit_bno055
import board
import time
import numpy as np
import matplotlib.pyplot as plt






class SensorData:

    data = [[0,0,0]]

    def __init__(self):
        print("hey i am created")
        print("hey i am created")
        print("hey i am created")

        x = self.data
        print(x)

        # i2c = board.I2C()
        # sensor = adafruit_bno055.BNO055_I2C(i2c)
        
        return None

    def update(self,frame):


        return lnx,lny,lnz


o = SensorData() 
print(o.data)

exit()










animation = FuncAnimation(fig, update, interval=50)
plt.show()
