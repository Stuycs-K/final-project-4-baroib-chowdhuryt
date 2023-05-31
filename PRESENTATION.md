# Audio Basics 
1. **Signals** represents audio as electrical or digital and carries sound information. It can be analog (continuous voltage variations) or digital (discrete numerical samples).
3. **Amplitude** represents the magnitude or strength of the audio signal. Higher amplitudes correspond to louder sounds, while lower amplitudes correspond to quieter sounds.
4. **Frequency** determines the pitch or tone of the audio signal. It is measured in Hertz (Hz) and corresponds to the number of cycles or vibrations per second.

 ![image](https://github.com/Stuycs-K/final-project-4-baroib-chowdhuryt/assets/90805264/1a6a950c-046f-4e61-acd4-200f870fa5db)
 
6. **Duration** length of time that an audio signal or sound lasts. Short durations represent brief sounds, while longer durations represent sustained sounds.
7. **Timbre** quality or character of a sound that distinguishes it from others. It is influenced by factors such as harmonic content, envelope, and spectral characteristics. It allows us to differentiate between different musical instruments or voices, even when they are playing the same note at the same volume.

## Analog Audio Signals:
   - Represented as variations in the amplitude (voltage) that correspond to changes in air pressure caused by sound waves.
   - Captured by microphones, converted into electrical voltage fluctuations, and transmitted as analog audio signals.
   - Speakers or headphones convert analog signals back into air pressure variations, reproducing the original sound.

## Digital Audio Signals:
   - Represented as a sequence of numerical samples, with each sample representing the amplitude at a specific time.
   - Samples are captured at regular intervals (sampling rate) and encoded as binary numbers (bits).
   - Digital audio enables accurate representation and reproduction of the original sound.

# Playing and Plotting Audio

from ```visualizer.py```:

1. ```playing_audio(file)``` This function is responsible for playing an audio file using the AudioSegment and play functions from the Pydub library. It takes the path of the audio file as input. First, it uses AudioSegment.from_wav to load the WAV file into an AudioSegment object called song. Then, it plays the audio using the play function, which plays the audio segment using the system's default audio player. If any error occurs, it prints the error message.
- ```Pydub``` is a Python library that provides a high-level interface for manipulating audio files. It is built on top of other audio processing libraries such as FFmpeg and Libav. Pydub allows you to perform various operations on audio files, such as slicing, concatenation, volume adjustment, and format conversion. The ```AudioSegment``` class from Pydub allows us to load, manipulate, export, and playback audio. 
2. ```showing_audiotrack(file)``` This function displays a plot of the audio waveform from a WAV file using the sf.read function from the soundfile library and the plot and related functions from the matplotlib library. It takes the path of the audio file as input. It first reads the audio data and sample rate from the WAV file using sf.read. It then retrieves the channel data from the audio data and assigns them to separate arrays (ch1 and ch2) for stereo audio. It creates the x-axis and y-axis values for plotting using np.linspace and the sample rate. It sets up the plot and updates it periodically based on the defined updatePeriodicity to show the progression of the audio track. The plot shows the audio waveform over time with a red line indicating the current position. If any error occurs, it prints the error message.
- ```Soundfile``` is a Python library that helps you read and write audio files. We used it to extract the audio data and sample rate from the WAV file. The returned values are assigned to the variables data and samplerate.

The variations in the signal properties encode various aspects of the sound, such as its intensity, frequency content, and temporal characteristics. These variations carry the information necessary to recreate the original sound wave and convey its characteristics, including pitch, timbre, dynamics, and spatial aspects. 

The most common representation of audio signals in code is an array of the amplitudes of the signal at a particular sample point in time. 
The **sampling rate** determines the number of samples taken per second, and the values of the samples represent the voltage levels of the electrical signal.

```samples = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5, -0.7, -0.9, -0.7, -0.5, -0.3, -0.1]```

```sample_rate = 44100```

- If the sample rate is 44100 Hz (samples per second), it means that 44100 amplitudes were recorded per second. Each amplitude value in the array corresponds to the amplitude of the audio signal at a specific sample point in time.

3. ```sr_convert(audio_file_path, new_sr)``` This function is used to resample an audio file to a new sample rate using the ```scipy.signal.resample``` function and then save the resampled audio as a new WAV file using the soundfile library.
- ```Scipy.signal``` is a powerful Python subpackage that helps with signal processing through tools to: filter, fourier transforms, convolution, spectrograms, generate waveforms, resample signals.
- It uses the ```signal.resample``` function from the ```scipy``` library to resample the audio data to the desired sample rate. It performs the resampling by interpolating the audio samples to create the new samples at the desired rate.
- It uses the ```sf_write``` function from the ```soundfile``` library to write the resampled audio data to the output file path with the desired sample rate.

According to the **Nyquist-Shannon sampling theorem**, to accurately capture and reproduce audio signals, the sampling rate must be at least twice the highest frequency present in the signal. This ensures that the original waveform can be reconstructed without significant loss of information.

### Fourier Transform
- We use the Fourier Transform to converts a signal from the time domain to the frequency domain- to convert our samples array to a waveform; it is a mathematical formula

![image](https://github.com/Stuycs-K/final-project-4-baroib-chowdhuryt/assets/90805264/155355e3-aeda-497e-b735-7f739f552335)

- It decomposes the audio signal into sine and cosine waves (harmonics) representing specific frequency components.
- Reveals frequency components and provides information about their magnitudes.

![image](https://github.com/Stuycs-K/final-project-4-baroib-chowdhuryt/assets/90805264/e9bc8e09-0e47-41fe-a062-88d8e28f1d07)

## Spectrum Analysis
- The output of the Fourier Transform is a spectrum representing the distribution of frequency components.
- Analyzing the spectrum helps identify dominant frequencies, harmonics, and other characteristics of the audio signal.

4. ```audio_diff(audio1_file, audio2_file)``` function compares two audio files to calculate and visualize the spectrogram difference between them using ```signal.spectrogram``` from ```scipy``` and ```matplotlib``` to show a spectrogram that is displayed as a color map, with logarithmic scaling of the magnitude difference. The resulting plot shows the difference in magnitude between the spectrograms in dB.
- ```signal.spectrogram``` takes in the audio signal, sample rate, type of window, length of each window in samples, overlap btwn. consecutive windows and mode of spectogram computation (magnitude, angle, power). 
- It then *windows* or tapers the edges of the signal to improve frequency resolution. For each windowed segment, the function applies a Fourier Transform to convert the signal to frequency components. 
- It calculates either the magnitude, angle, or power spectrum of each segment. The power spectrum represents the distribution of signal power across different frequencies. 
  - Magnitude: The magnitude represents the strength or amplitude of the frequency component. It indicates how much energy or     power is present at a particular frequency. The magnitude spectrum is often used to analyze the frequency content of an audio   signal. It provides information about the intensity or loudness of different frequency components.
  - Angle: The angle, also known as the phase, represents the phase shift of the frequency component. It indicates the relative   timing or alignment of the sinusoidal component with respect to a reference point. The phase spectrum is useful for             analyzing the temporal characteristics and synchronization of different frequency components.
  - Power: The power spectrum represents the power of the frequency component. It is calculated by squaring the magnitude         spectrum. The power spectrum provides a measure of the energy distribution across different frequencies in the audio signal.   It is commonly used in applications such as audio equalization and filtering.

- Finally, to smooth the spectrogram and reduce the effects of windowing on the frequency resolution, the function uses overlap between segments. It combines the power spectra of adjacent segments by averaging them. It returns:
  - f: The array of frequency points corresponding to the rows of the spectrogram.
  - t: The array of time points corresponding to the columns of the spectrogram.
  - Sxx: The 2-D array containing the spectrogram values. Each element represents the power or magnitude of the frequency
    component at a specific time and frequency   

# WAV FILES (Waveform Audio File Format) 
1. **Header** WAV files begin with a header containing metadata about the audio file. Metadata includes format, encoding parameters, sample rate, number of channels, etc.
2. **Audio Data** Follows the header and contains the actual audio samples representing amplitude over time.
3. **Sample Rate and Bit Depth** Sample rate determines the number of samples captured per second, defining the time resolution. Bit depth specifies the number of bits used to represent each sample, affecting dynamic range and precision.
4. **Channels and Compression** WAV files support different channel configurations (e.g., mono, stereo). They typically store uncompressed audio data, resulting in large file sizes. Metadata can also be included in WAV files, providing additional descriptive information about the audio.

*run ```make audio_track ARGS="src/sample1.wav"``` to play audio from src/sample1.wav and view its waveform* 

# FREQUENCY MODULATION
Frequency modulation (FM) is the encoding of information in a carrier wave by varying the instantaneous frequency of the wave. The modulation index is the ratio of the frequency deviation of the modulated signal to the message signal bandwidth. Our FM has a deviation of 1. Typically the carrier signal has constant amplitude, frequency, and phase. Since our audios aren't constant, we modulated every one second of the fifteen seconds of two audios and concatenated it. Our FM audio has varying amplitudes and frequencies.  

![image](https://github.com/Stuycs-K/final-project-4-baroib-chowdhuryt/assets/73133134/b0713c34-196a-41a3-add3-cef508d0902f)

*run ```make audio_diff ARGS="src/sample1.wav src/sample2.wav"``` to view the spectrogram difference of audio1 and audio2*


*run ```make frequency_mod ARGS="src/sample1.wav src/sample2.wav"``` to view the modulated audio of audio1 and audio2*
