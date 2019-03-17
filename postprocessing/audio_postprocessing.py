"""

This module implements an abstract class for audio postprocessing

"""
class AudioPostprocessing():
    """Abstract class for audio postprocessing.

    Audio postprocessing is applied per audio stream after
    the pitch processing. 

    """

    def apply(self, data, channels, frequency, max):
        """Called to apply the post process effect on audio data.

        Args:
            data (int): The audio samples of the stream. May contain multiple
                channels. The data is signed.
            channels (int): The number of channels in the audio data.
            frequency (int): The frequency of the audio data.
            max (int): The maximum allowed range for the format. Depends on the sample
                size. (For 16 bit the maximum value is 32767). Everything outside
                this range will be clamped to the maximum value.

        Return:
            The processed data as a list.
        """
        raise NotImplementedError("Class %s doesn't implement apply()" % (self.__class__.__name__))