import numpy as np
import matplotlib.pyplot as plt
from math import pi
import soundfile as sf
from scipy.fft import *
from scipy.io import wavfile


def freq(file, start_time, end_time):
    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass
    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr / 1000) : int(end_time * sr / 1000) + 1]
    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)
    # frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()
    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq

plt.close('all')

sample1 = freq("source_file.wav", 0, 15000) #carrier
sample2 = freq("sample-15s.wav", 0, 15000) #modulator

# Setting up FM modulation simulation parameters
Fs = 2000
t = np.arange(0,0.2,1/Fs)
fc = sample1 # carrier frequency
fm1 = sample2 # Signal frequency-1 to construct message signal
b = 1 # modulation index

m_signal = np.sin(2*pi*fm1*t)
carrier_signal = np.sin(2 * pi * fc * t)
# Generate Frequency modulated signal
fmd = np.sin(2*pi*fc*t + b*m_signal)


# Plots
plt.subplot(3,1,1)
plt.plot(t, m_signal)
plt.title("Modulator Signal")

plt.subplot(3,1,2)
plt.plot(t, carrier_signal)
plt.title("Message Carrier Signal")

plt.subplot(3,1,3)
plt.plot(t, fmd)
plt.title("Frequency Modulated Signal")

plt.tight_layout()
plt.show()
