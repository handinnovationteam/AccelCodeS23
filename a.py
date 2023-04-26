import adafruit_bno055
import board
import time
import numpy as np
import matplotlib.pyplot as plt

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

data = []
plt.axis([0,10,0,1])

for i in range(200):
	print(sensor.temperature)
	print(sensor.euler)
	print(sensor.gravity)
	data.append(sensor.gravity)
	print()

	datanp = np.array(data)
	plt.plot(datanp[:,0])
	plt.plot(datanp[:,1])
	plt.plot(datanp[:,2])
	print(datanp[:,0])
	plt.pause(0.05)

plt.show()




# np.swapaxes
