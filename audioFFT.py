# attempt of Fourier Transform combined with our data from i2c

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



plt.ion()
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# start of olivia questionable code
RATE = 44100

CHUNK = 2048 # RATE / number of updates per second

window = np.blackman(CHUNK)

RECORD_SECONDS = 20
def soundPlot(stream):
    t1=time.time()
    # data = stream.read(CHUNK, exception_on_overflow=False)
    # waveData = wave.struct.unpack("%dh"%(CHUNK), data)
    # npArrayData = np.array(waveData)

    npArrayData = np.random.random((2048)) * 2000

    indata = npArrayData*window
    #Plot time domain
    ax1.cla()
    ax1.plot(indata)
    ax1.grid()
    ax1.axis([0,CHUNK,-5000,5000])
    fftData=np.abs(np.fft.rfft(indata))
    fftTime=np.fft.rfftfreq(CHUNK, 1./RATE)
    which = fftData[1:].argmax() + 1
    #Plot frequency domain graph
    ax2.cla()
    ax2.plot(fftTime,fftData)
    ax2.grid()
    ax2.axis([0,5000,0,10**6])
    plt.pause(0.0001)
    print("took %.02f ms"%((time.time()-t1)*1000))
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/CHUNK
        print ("The freq is %f Hz." % (thefreq))
    else:
        thefreq = which*RATE/CHUNK
        print ("The freq is %f Hz." % (thefreq))

for i in range(100):
    soundPlot(None)
