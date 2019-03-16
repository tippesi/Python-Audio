from postprocessing.audio_postprocessing import AudioPostprocessing

class VolumePostprocessing(AudioPostprocessing):

    def __init__(self, volume = 1.0):
        self.volume = volume

    def apply(self, data, channels, frequency):
        for i in range(0, len(data)):
            data[i] = int(float(data[i]) * self.volume)

        return data