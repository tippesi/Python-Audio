from postprocessing.audio_postprocessing import AudioPostprocessing

import time
import math

class ChannelSinePostprocessing(AudioPostprocessing):

    def __init__(self, speed = 1.0):
        self.starttime = time.clock()
        self.speed = speed

    def apply(self, data, channels, frequency):

        deltatime = (time.clock() - self.starttime) * self.speed

        # We want two channels to work with
        if channels is not 2:
            return

        leftVolume = 0.5 * math.sin(deltatime) + 0.5
        rightVolume = 1.0 - leftVolume

        # print(leftVolume)

        for i in range(0, len(data)):
            """
            if i % 2:
                data[i] = int(float(data[i]) * leftVolume)
            else:
                data[i] = int(float(data[i]) * rightVolume)
            """
            data[i] = data[i] & 255

        return data