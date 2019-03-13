import audio
from postprocessing.volume_postprocessing import VolumePostprocessing
import pyaudio

paudio = pyaudio.PyAudio()

audio = audio.Audio("MenuTheme2_final.wav", 1024, paudio)

audio.postprocessing.append(VolumePostprocessing(10.0))

while True:
    audio.update()

paudio.terminate()