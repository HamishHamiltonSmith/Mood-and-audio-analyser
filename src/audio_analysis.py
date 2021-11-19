from matplotlib import pyplot as plt
from scipy.io.wavfile import read
import numpy as np
from scipy.fft import fft,fftfreq




def analyse(file):
    rate=4400
    _,data = read(str(file))
    duration = len(data)/rate
    N = rate*duration
    time = np.arange(0,duration,1/rate)
    yf = fft(data)
    xf = fftfreq(int(N),1 / rate)
    fig, axs = plt.subplots(2)
    axs[0].plot(abs(xf),abs(yf))
    axs[1].plot(time,data)
    plt.show()

if __name__ == "__main__":
    analyse(1)



