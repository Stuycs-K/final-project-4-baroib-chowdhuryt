# AUDIO VISUALIZATION & FREQUENCY MODULATION

## Energetic Dodgers : Bernadette Baroi, Tasnim Chowdhury

### This project focuses on audio visualization techniques, providing functionalities for playing audio files, visualizing their waveforms, and analyzing spectrogram differences. It includes a frequency modulation simulation that showcases the effects of modulating frequencies on carrier signals, enhancing understanding of audio processing techniques and frequency modulation concepts.

### HOW TO USE
1. Clone the repo on your own computer, not the lab machines since there are issues with getting the libraries
2. Run ```make install_libs``` to install required libraries. Then run  ```sudo apt install ffmpeg``` and ```sudo apt-get install python3-tk```.
3. Audio Visualization
- Use our sample audios from the ```src/``` directory or find your own from [here](https://soundbible.com/)
- Play audio from audio1.wav and view its waveform. This function refreshes every 2 seconds. 

```make audio_track ARGS="[path to audio1.wav]"``` 
  
- Viewing the differences in waveforms between audio1.wav and audio2.wav.  This function can only take in mono/stereo audio and can only plot for as long as the shorter audio. 

```make audio_diff ARGS="[path to audio1.wav] [path to audio2.wav]"```
  
4. Frequency Modulation

```make frequency_mod ARGS="[path to audio1.wav] [path to audio2.wav]"```

### [PRESENTATION](PRESENTATION.md)

### [HOMEWORK](HOMEWORK.md)
