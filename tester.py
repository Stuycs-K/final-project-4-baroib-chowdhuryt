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
