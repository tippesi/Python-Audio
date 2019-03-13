import pyaudio
import wave
import struct
import sys
import math

class Audio:
    """

    """
    def __init__(self, filename, chunksize, paudio):
        filestream = wave.open(filename, "rb")

        self.audiostream = paudio.open(format = paudio.get_format_from_width(filestream.getsampwidth()),  
                channels = filestream.getnchannels(),  
                rate = filestream.getframerate(),  
                output = True)

        self.progress = 0.0
        self.pitch = 1.0
        self.volume = 1.0
        self.chunksize = chunksize

        # We store the data as integers here
        self.audiodata = []

        # These formats should work most of the time
        # See: https://docs.python.org/2/library/struct.html#format-characters
        types = {1: 'B', 2: 'h', 4: 'i'}
        self.type = types[filestream.getsampwidth()]
        # Check for system byteorder
        endianness = {"big": '>', "little": '<'}
        self.endianness = endianness[sys.byteorder]

        audiodata = filestream.readframes(chunksize)

        while(audiodata):
            fmt = self.endianness + self.type * int(len(audiodata) / filestream.getsampwidth()) 
            data = struct.unpack(fmt, audiodata)
            self.audiodata.extend(data)
            audiodata = filestream.readframes(chunksize)

        filestream.close()

        while(True):
            self.process()

    def __del__(self):
        self.audiostream.stop_stream()
        self.audiostream.close()

    def process(self):
        if (self.progress > len(self.audiodata)):
            return
        readout = self.pitch * float(self.chunksize)
        index = math.floor(self.progress)
        count = math.ceil(readout)
        subdata = self.audiodata[index : min(index + count, len(self.audiodata))]
        fmt = self.endianness + self.type * len(subdata)
        audiodata = struct.pack(fmt, *subdata)
        self.audiostream.write(audiodata)
        self.progress += readout

paudio = pyaudio.PyAudio()

audio = Audio("MenuTheme2_final.wav", 1024, paudio)

paudio.terminate()