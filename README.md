# AUDIO VISUALIZATION & FREQUENCY MODULATION

### This project focuses on audio visualization techniques, providing functionalities for playing audio files, visualizing their waveforms, and analyzing spectrogram differences. It includes a frequency modulation simulation that showcases the effects of modulating frequencies on carrier signals, enhancing understanding of audio processing techniques and frequency modulation concepts.

### HOW TO USE
1. Clone the repo. If on the lab machines, ssh into either marge or cslab4-?? or cslab4-??. 
2. Run ```make install_libs``` to install required libraries. Run  ```sudo apt install ffmpeg``` and ```sudo apt-get install python3-tk``` if not on lab machines.
3. Audio Visualization
- Use our sample audios from the ```src/``` directory or find your own from [link]
- Play audio from audio1.wav and view its waveform ```make audio_track ARGS="[path to audio1.wav]"``` 
- Viewing the differences in waveforms between audio1.wav and audio2.wav ```make audio_diff ARGS="[path to audio1.wav] [path to audio2.wav]"``` 
5. Frequency Modulation

### PRESENTATION

### HOMEWORK
