audio_track :
	@python3 visualizer.py "single" $(ARGS)

audio_diff :
	@python3 visualizer.py "double" $(ARGS)

frequency_mod :
	@python3 visualizer.py "FMdouble" $(ARGS)

install_libs :
	@pip3 install matplotlib
	@pip3 install soundfile
	@pip3 install pydub
	@pip3 install librosa
	@pip3 install scipy
	#sudo apt install ffmpeg
	#sudo apt install python3-tk
