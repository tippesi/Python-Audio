"""
Abstract class for audio postprocessing.
Audio postprocessing is applied per audio stream
after the pitch processing.
"""
class AudioPostprocessing():

    """
    
    """
    def apply(self, data, channels, frequency):
        raise NotImplementedError("Class %s doesn't implement apply()" % (self.__class__.__name__))