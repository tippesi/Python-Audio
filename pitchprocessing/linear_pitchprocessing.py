from pitchprocessing.pitchprocessing import PitchProcessing

import math

class LinearPitchProcessing(PitchProcessing):

    def apply(self, data, progress, count, channels, frequency):
        processeddata = [0] * count

        for i in range(0, int(count / channels)):
            for j in range(0, channels):
                lowerindex = int(math.floor(progress)) * channels + j
                upperindex = int(math.ceil(progress)) * channels + j

                remainder = progress - math.floor(progress)

                lowervalue = float(data[lowerindex])
                uppervalue = float(data[upperindex])

                # Linear interpolation of data points
                value = int(lowervalue + (uppervalue - lowervalue) * remainder)

                processeddata[i * channels + j] = value

            progress += self.pitch

        return processeddata