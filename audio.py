# External imports
import pyaudio
import wave
import struct
import sys
import math

# Internal imports
import postprocessing.audio_postprocessing
from pitchprocessing.linear_pitchprocessing import LinearPitchProcessing

class Audio():
    """

    """

    def __init__(self, filename, chunksize, paudio):

        filestream = wave.open(filename, "rb")

        self._audiostream = paudio.open(format = paudio.get_format_from_width(filestream.getsampwidth(), False),  
                channels = filestream.getnchannels(),  
                rate = filestream.getframerate(),  
                output = True)

        self.progress = 0.0
        self.loop = False
        self.channels = filestream.getnchannels()
        self.frequency = filestream.getframerate()
        self.postprocessing = []
        self.pitchprocessor = LinearPitchProcessing(1.0)

        self._chunksize = chunksize

        # All the formats we accept are signed
        self._maxvalue = int(pow(2, 8 * filestream.getsampwidth() - 1)) - 1

        # We store the data as integers here
        self._audiodata = []

        # These formats should work most of the time
        # See: https://docs.python.org/2/library/struct.html#format-characters
        types = {1: 'b', 2: 'h', 4: 'i'}
        endianness = {"big": '>', "little": '<'}

        # Checl for data type here
        self._type = types[filestream.getsampwidth()]

        # Check for system byteorder
        self._endianness = endianness[sys.byteorder]

        audiodata = filestream.readframes(chunksize)

        # Copy byte data to integer list
        while(audiodata):
            fmt = self._endianness + self._type * int(len(audiodata) / filestream.getsampwidth())
            data = struct.unpack(fmt, audiodata)
            self._audiodata.extend(data)
            audiodata = filestream.readframes(chunksize)

        filestream.close()

    def __del__(self):
        self._audiostream.stop_stream()
        self._audiostream.close()

    def update(self):
        # Check if playback should be in a loop
        if self.loop:
            self.progress = self.progress % float(len(self._audiodata))
        else:
            if self.progress >= len(self._audiodata):
                return

        chunksize = min(self._chunksize, int(math.floor((len(self._audiodata) - math.ceil(self.progress)
             * self.channels) / self.pitchprocessor.pitch)))

        # Apply pitch processor here
        subdata = self.pitchprocessor.apply(self._audiodata, self.progress, chunksize,
            self.channels, self.frequency)

        # Apply post-processing here
        for postprocessor in self.postprocessing:
            subdata = postprocessor.apply(subdata, self.channels, self.frequency, self._maxvalue)

        # Check if values are in their specified range
        for i in range(0, len(subdata)):
            subdata[i] = max(min(subdata[i], self._maxvalue), -self._maxvalue)
        
        fmt = self._endianness + self._type * len(subdata)
        audiodata = struct.pack(fmt, *subdata)
        self._audiostream.write(audiodata)
        self.progress += self.pitchprocessor.pitch * float(chunksize / self.channels)