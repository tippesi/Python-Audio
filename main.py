import audio
import pyaudio

paudio = pyaudio.PyAudio()

audio = audio.Audio("MenuTheme2_final.wav", 1024, paudio)

audio.volume = 2.0

while True:
    audio.update()

paudio.terminate()