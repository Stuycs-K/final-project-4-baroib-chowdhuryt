# Audio Basics 
1. **Signals** represents audio as electrical or digital and carries sound information. It can be analog (continuous voltage variations) or digital (discrete numerical samples).
3. **Amplitude** represents the magnitude or strength of the audio signal. Higher amplitudes correspond to louder sounds, while lower amplitudes correspond to quieter sounds.
4. **Frequency** determines the pitch or tone of the audio signal. It is measured in Hertz (Hz) and corresponds to the number of cycles or vibrations per second.

 ![image](https://github.com/Stuycs-K/final-project-4-baroib-chowdhuryt/assets/90805264/1a6a950c-046f-4e61-acd4-200f870fa5db)
 
6. **Duration** length of time that an audio signal or sound lasts. Short durations represent brief sounds, while longer durations represent sustained sounds.
7. **Timbre** quality or character of a sound that distinguishes it from others. It is influenced by factors such as harmonic content, envelope, and spectral characteristics.

## Analog Audio Signals:
   - Represented as variations in the amplitude (voltage) that correspond to changes in air pressure caused by sound waves.
   - Captured by microphones, converted into electrical voltage fluctuations, and transmitted as analog audio signals.
   - Speakers or headphones convert analog signals back into air pressure variations, reproducing the original sound.

## Digital Audio Signals:
   - Represented as a sequence of numerical samples, with each sample representing the amplitude at a specific time.
   - Samples are captured at regular intervals (sampling rate) and encoded as binary numbers (bits).
   - Digital audio enables accurate representation and reproduction of the original sound.

# Plotting Audio
The variations in the signal properties encode various aspects of the sound, such as its intensity, frequency content, and temporal characteristics. These variations carry the information necessary to recreate the original sound wave and convey its characteristics, including pitch, timbre, dynamics, and spatial aspects.

The most common representation of audio signals in code is an array of the amplitudes of the signal at a particular sample point in time. 
The **sampling rate** determines the number of samples taken per second, and the values of the samples represent the voltage levels of the electrical signal.

```samples = [0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.7, 0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5, -0.7, -0.9, -0.7, -0.5, -0.3, -0.1]```

```sample_rate = 44100```

- If the sample rate is 44100 Hz (samples per second), it means that 44100 amplitudes were recorded per second. Each amplitude value in the array corresponds to the amplitude of the audio signal at a specific sample point in time.

According to the **Nyquist-Shannon sampling theorem**, to accurately capture and reproduce audio signals, the sampling rate must be at least twice the highest frequency present in the signal. This ensures that the original waveform can be reconstructed without significant loss of information.

### Fourier Transformation
- We use the Fourier Transformation to converts a signal from the time domain to the frequency domain- to convert our samples array to a waveform
- It decomposes the audio signal into sine and cosine waves (harmonics) representing specific frequency components.
- Reveals frequency components and provides information about their magnitudes.

## Spectrum Analysis
- The output of the Fourier Transform is a spectrum representing the distribution of frequency components.
- Analyzing the spectrum helps identify dominant frequencies, harmonics, and other characteristics of the audio signal.

# WAV FILES (Waveform Audio File Format) 
1. **Header** WAV files begin with a header containing metadata about the audio file. Metadata includes format, encoding parameters, sample rate, number of channels, etc.
2. **Audio Data** Follows the header and contains the actual audio samples representing amplitude over time.
3. **Sample Rate and Bit Depth** Sample rate determines the number of samples captured per second, defining the time resolution. Bit depth specifies the number of bits used to represent each sample, affecting dynamic range and precision.
4. **Channels and Compression** WAV files support different channel configurations (e.g., mono, stereo). They typically store uncompressed audio data, resulting in large file sizes. Metadata can also be included in WAV files, providing additional descriptive information about the audio.

*run ```make audio_track ARGS="src/sample1.wav"``` to play audio from src/sample1.wav and view its waveform* 

# FREQUENCY MODULATION
*run ```make audio_diff ARGS="src/sample1.wav src/sample2.wav"``` to view the differences between audio1 and audio2* 

The modulation index is the ratio of the frequency deviation of the modulated signal to the message signal bandwidth. Takes the dominant frquency in both wav files to FM
