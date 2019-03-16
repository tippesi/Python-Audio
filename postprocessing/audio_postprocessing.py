"""

This module implements an abstract class for audio postprocessing

"""
class AudioPostprocessing():
    """Abstract class for audio postprocessing.

    Audio postprocessing is applied per audio stream after
    the pitch processing. 

    """

    def apply(self, data, channels, frequency):
        """Called to apply the post process effect on audio data.

        Args:
            data (int): The audio samples of the stream. May contain multiple
                channels.
            channels (int): The number of channels in the audio data.
            frequency (int): The frequency of the audio data.

        """
        raise NotImplementedError("Class %s doesn't implement apply()" % (self.__class__.__name__))