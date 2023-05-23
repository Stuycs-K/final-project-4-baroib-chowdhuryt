# IMPORTING PACKAGES

import time
from multiprocessing import Process

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import soundfile as sf
import librosa

from pydub import AudioSegment
from pydub.playback import play


# PREPARING THE AUDIO DATA

# Audio file, .wav file
wavFile = "source_file.wav"

# Retrieve the data from the wav file
data, samplerate = sf.read(wavFile)

n = len(data)  # the length of the arrays contained in data
Fs = samplerate  # the sample rate

# Working with stereo audio, there are two channels in the audio data.
# Let's retrieve each channel seperately:
ch1 = np.array([data[i][0] for i in range(n)])  # channel 1
ch2 = np.array([data[i][1] for i in range(n)])  # channel 2

# x-axis and y-axis to plot the audio data
time_axis = np.linspace(0, n / Fs, n, endpoint=False)
sound_axis = ch1

# plt.plot(time_axis, sound_axis)
# plt.show()

def playing_audio():
    try:
        song = AudioSegment.from_wav(wavFile)
        play(song)
    except Exception as e:
        print("Error playing audio:", str(e))


def showing_audiotrack():
    try:
        # We use a variable previousTime to store the time when a plot update is made
        # and to then compute the time taken to update the plot of the audio data.
        previousTime = time.time()

        # Turning the interactive mode on
        plt.ion()

        # Each time we go through a number of samples in the audio data that corresponds to one second of audio,
        # we increase spentTime by one (1 second).
        spentTime = 0

        # Let's the define the update periodicity
        updatePeriodicity = 2 # expressed in seconds

        # Plotting the audio data and updating the plot
        for i in range(n):
            # Each time we read one second of audio data, we increase spentTime :
            if i // Fs != (i-1) // Fs:
                spentTime += 1
            # We update the plot every updatePeriodicity seconds
            if spentTime == updatePeriodicity:
                # Clear the previous plot
                plt.clf()
                # Plot the audio data
                plt.plot(time_axis, sound_axis)
                # Plot a red line to keep track of the progression
                plt.axvline(x=i / Fs, color='r')
                plt.xlabel("Time (s)")
                plt.ylabel("Audio")
                plt.show()  # shows the plot
                plt.pause(updatePeriodicity-(time.time()-previousTime))
                # a forced pause to synchronize the audio being played with the audio track being displayed
                previousTime = time.time()
                spentTime = 0
    except Exception as e:
        print("Error showing audio track:", str(e))

def sr_convert(audio1, new_sr=44100):
    # Resample the audio to the new sample rate in Hz
    y, sr = librosa.load(audio1, sr=None)
    y_resampled = librosa.resample(y, sr, new_sr)

    # Save the resampled audio as a new file
    output_path = audio1 +'_new.wav'
    librosa.output.write_wav(output_path, y_resampled, new_sr)
    return output_path

def audio_diff(audio1, audio2):
    try:
         # Read the audio data from the WAV files
        audio1, samplerate1 = sf.read(audio1_file)

        # Ensure that the sample rates are the same
        audio2 = sr_convert(audio2, samplerate1)
        audio2, samplerate2 = sf.read(audio2_file)

        if samplerate1 != samplerate2:
            print("Error: Sample rates of the audio files do not match.")
            exit(1);

        samplerate = samplerate1

        window = signal.windows.hann(256)
        nperseg = 256  # samples per segment
        nooverlap = 128  # overlap between segments

        #Use the fourier transformation
        _, _, spectrogram1 = signal.spectrogram(audio1, fs=sample_rate, window=window, nperseg=nperseg, noverlap=nooverlap)
        _, _, spectrogram2 = signal.spectrogram(audio2, fs=sample_rate, window=window, nperseg=nperseg, noverlap=nooverlap)

        spectrogram_diff = spectrogram1 - spectrogram2

        # Visualize the difference spectrogram
        plt.imshow(spectrogram_diff, aspect='auto', origin='lower', cmap='coolwarm')
        plt.colorbar(label='Magnitude difference')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.title('Spectrogram Difference')
        plt.show()
    except Exception as e:
        print("Error calculating audio difference:", str(e))


if __name__ == "__main__":
    p1 = Process(target=playing_audio, args=())
    p1.start()
    p2 = Process(target=showing_audiotrack, args=())
    p2.start()
    p1.join()
    p2.join()

    #audio_diff(audio1, audio2)
