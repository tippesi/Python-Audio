from audio import Audio
from postprocessing.volume_postprocessing import VolumePostprocessing
from postprocessing.channel_sine_postprocessing import ChannelSinePostprocessing
import pyaudio

paudio = pyaudio.PyAudio()

audio = Audio("MenuTheme2_final.wav", 2048, paudio)

# Append postprocessing effects
# audio.postprocessing.append(VolumePostprocessing(0.5))
# audio.postprocessing.append(ChannelSinePostprocessing(0.5))

# The pitch processor is variable and can be changed if needed
# The default processor is the linear pitch-processor. This method
# might lead to sabertooth like audio data.
audio.pitchprocessor.pitch = 0.9

while True:
    audio.update()

paudio.terminate()