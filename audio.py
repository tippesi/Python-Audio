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

        self._audiostream = paudio.open(format = paudio.get_format_from_width(filestream.getsampwidth()),  
                channels = filestream.getnchannels(),  
                rate = filestream.getframerate(),  
                output = True)

        self.progress = 0.0
        self.pitch = 1.0
        self.volume = 1.0
        self._chunksize = chunksize

        # We store the data as integers here
        self._audiodata = []

        # These formats should work most of the time
        # See: https://docs.python.org/2/library/struct.html#format-characters
        types = {1: 'B', 2: 'h', 4: 'i'}
        self._type = types[filestream.getsampwidth()]
        # Check for system byteorder
        endianness = {"big": '>', "little": '<'}
        self._endianness = endianness[sys.byteorder]

        audiodata = filestream.readframes(chunksize)

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
        self.progress = self.progress % float(len(self._audiodata))        
        readout = self.pitch * float(self._chunksize)
        index = math.floor(self.progress)
        count = math.ceil(readout)
        subdata = self._audiodata[index : min(index + count, len(self._audiodata))]
        fmt = self._endianness + self._type * len(subdata)
        audiodata = struct.pack(fmt, *subdata)
        self._audiostream.write(audiodata)
        self.progress += readout