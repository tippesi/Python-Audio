from audio import Audio
from postprocessing.volume_postprocessing import VolumePostprocessing
from postprocessing.channel_sine_postprocessing import ChannelSinePostprocessing
import pyaudio

paudio = pyaudio.PyAudio()

audio = Audio("MenuTheme2_final.wav", 2048, paudio)

# audio.postprocessing.append(VolumePostprocessing(1.0))
audio.postprocessing.append(ChannelSinePostprocessing(0.5))

while True:
    audio.update()

paudio.terminate()