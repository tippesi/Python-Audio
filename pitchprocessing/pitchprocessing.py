"""

This module implements an abstract class for audio postprocessing

"""
class PitchProcessing():
    """Abstract class for pitch postprocessing.

    Pitch postprocessing is applied per audio stream before
    the audio processing. 

    Attributes:
        pitch (float): The speed factor at which the audio is played

    """
    def __init__(self, pitch = 1.0):
        """

        """
        self.pitch = pitch


    def apply(self, data, progress, count, channels, frequency):
        """Called to apply the pitch process on audio data.

        Args:
            data (int): The audio samples of the stream. May contain multiple
                channels. The data is signed.
            progress (float): The progress in the data stream in range (0, len(data))
            count (int): The number of expected samples in the return data.
            channels (int): The number of channels in the audio data.
            frequency (int): The frequency of the audio data.
        
        Return:
            The processed data as a list
        """
        raise NotImplementedError("Class %s doesn't implement apply()" % (self.__class__.__name__))