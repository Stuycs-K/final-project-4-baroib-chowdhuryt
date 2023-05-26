import time
from multiprocessing import Process

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

import soundfile as sf
from librosa import resample, load
from soundfile import write as sf_write

from pydub import AudioSegment
from pydub.playback import play
from scipy import signal

def playing_audio(file):
    try:
        song = AudioSegment.from_wav(file)
        play(song)
    except Exception as e:
        print("Error playing audio:", str(e))

def showing_audiotrack(file):
    try:
         # Retrieve the data from the wav file
        data, samplerate = sf.read(file)

        n = len(data)  # the length of the arrays contained in data
        Fs = samplerate  # the sample rate

        # Working with stereo audio, there are two channels in the audio data.
        # Let's retrieve each channel seperately:
        ch1 = np.array([data[i][0] for i in range(n)])  # channel 1
        ch2 = np.array([data[i][1] for i in range(n)])  # channel 2

        # x-axis and y-axis to plot the audio data
        time_axis = np.linspace(0, n / Fs, n, endpoint=False)
        sound_axis = ch1

        # store the time when a plot update is made + compute the time taken to update the plot of the audio data.
        previousTime = time.time()
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

def run_audio_processes(wavFile):
    p1 = Process(target=playing_audio, args=(wavFile,))
    p1.start()
    p2 = Process(target=showing_audiotrack, args=(wavFile,))
    p2.start()
    p1.join()
    p2.join()

def sr_convert(audio_file_path, new_sr):
    # Load the audio file with its original sample rate
    audio_data, orig_sr = load(audio_file_path, sr=None)

    # Calculate the number of samples required in the resampled audio data
    num_samples_required = int(round(len(audio_data) * new_sr / orig_sr))

    # Use scipy.signal.resample to resample
    y_resampled = signal.resample(audio_data, num_samples_required)

    # Save the resampled audio data as a new wav file
    output_file_path = audio_file_path.rstrip('.wav') + '_resampled.wav'
    sf_write(output_file_path, y_resampled, new_sr)

    return output_file_path

def audio_diff(audio1_file, audio2_file):
    try:
        # Read the audio data from the WAV files
        audio1, samplerate1 = sf.read(audio1_file)
        audio2, samplerate2 = sf.read(audio2_file)

        # Check if audio files have the same sample rate
        if samplerate1 != samplerate2:
            print("Resampling the second audio file to match the first one.")
            audio2_file = sr_convert(audio2_file, samplerate1)
            audio2, samplerate2 = sf.read(audio2_file)

        samplerate = samplerate1

        # Flatten stereo audio into mono for simplicity
        if audio1.ndim > 1:
            audio1 = np.mean(audio1, axis=1)
        if audio2.ndim > 1:
            audio2 = np.mean(audio2, axis=1)

        # Trim or extend the audio files to the same length
        min_length = min(len(audio1), len(audio2))
        audio1 = audio1[:min_length]
        audio2 = audio2[:min_length]
        print("Trimming the longer audio file to match the shorter one's length.")

        # Determine the window size and overlap
        window_size = min(512, min_length)  # Adjust window size if audio is shorter
        overlap = window_size // 2

        # Use the Fourier transformation to get the spectrograms
        _, _, spectrogram1 = signal.spectrogram(audio1, fs=samplerate, window='hann', nperseg=window_size, noverlap=overlap, mode='magnitude')
        _, _, spectrogram2 = signal.spectrogram(audio2, fs=samplerate, window='hann', nperseg=window_size, noverlap=overlap, mode='magnitude')

        # Compute the spectrogram difference
        spectrogram_diff = np.abs(spectrogram1 - spectrogram2)

        # Visualize the difference spectrogram
        plt.imshow(10 * np.log10(spectrogram_diff + 1e-10), aspect='auto', origin='lower', cmap='coolwarm')
        plt.colorbar(label='Magnitude difference (dB)')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.title('Spectrogram Difference')
        plt.show()
    except Exception as e:
        print("Error calculating audio difference:", str(e))

if __name__ == "__main__":
    """
    wavFile = "src/source_file.wav"
    run_audio_processes(wavFile)
    """

    """
    audio1 = 'src/sample-15s.wav'
    audio2 = 'src/source_file.wav'
    audio_diff(audio1, audio2)
    """
