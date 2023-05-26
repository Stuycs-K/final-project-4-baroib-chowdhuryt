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
































"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

car = "source_file.wav"
modu = "sample-15s.wav"

sample1 = sf.read(car)
sample2 = sf.read(modu)

A_c = 1                     # Carrier amplitude
f_c = sample1              # Carrier frequency
f_m = sample2               # Modulation frequency
A_m = 1                     # Modulation amplitude
fd = 4                      # Frequency deviation

t_max = 4
fs = 100
t = np.linspace(0, t_max, t_max*fs)
#data = -np.cos(2*np.pi * 1 * t)
# Carrier and modulation signals definition
carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)

# FM signal
dt = t[1]-t[0]
fm = A_c*np.cos(2*np.pi*f_c*t+2*np.pi*fd*np.cumsum(modulator*dt))

plt.plot(t, fm)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

plt.plot(t, data)
intended_freq_approx = np.hstack([0, *np.diff([data])])
intended_freq_approx *= np.abs(data).max() / np.abs(intended_freq_approx).max()
plt.plot(t, intended_freq_approx)

plt.legend(['FM Signal', 'Original Signal', '~Intended Freq'])
plt.show()

"""
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

car = "source_file.wav"
modu = "sample-15s.wav"

sample1 = sf.read(car)
sample2 = sf.read(modu)

A_c = 1                     # Carrier amplitude
f_c = sample1               # Carrier frequency
f_m = sample2               # Modulation frequency
A_m = 1                     # Modulation amplitude
fd = 4                      # Frequency deviation

t_max = 4
fs = 100
t = np.linspace(0, t_max, t_max*fs)

# Carrier and modulation signals definition
carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)

# FM signal
dt = t[1]-t[0]
fm = A_c*np.cos(2*np.pi*f_c*t+2*np.pi*fd*np.cumsum(modulator*dt))
"""

"""
import numpy as np
import matplotlib.pyplot as plt

#%% Generate #################################################################

t = np.linspace(0, 1, 2048, 0)
fc = 200
b = 15
data = -np.cos(2*np.pi * 1 * t)
phi = fc*t + b * data
fm = np.sin(2*np.pi * phi)


#%% Plot #####################################################################
plt.plot(t, fm)
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.plot(t, data)
intended_freq_approx = np.hstack([0, *np.diff([data])])
intended_freq_approx *= np.abs(data).max() / np.abs(intended_freq_approx).max()
plt.plot(t, intended_freq_approx)
plt.legend(['FM Signal', 'Original Signal', '~Intended Freq'])
plt.show()

#%% Bonus ####################################################################
from ssqueezepy import ssq_stft
from ssqueezepy.visuals import imshow

Tx = ssq_stft(fm)[0][::-1]
imshow(Tx, abs=1, title="abs(SSQ_STFT)", ylabel="frequency", xlabel="time",
       ticks=0)
"""
