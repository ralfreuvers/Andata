# External Library Imports
import librosa

# Class Definition
class andatum:
    def __init__(self,filepath):
        # Load song file into self, store the total waveform & sample rate
        self.filepath = filepath
        self.tseries, self.sr = librosa.load(filepath, sr=None)

        # randomly assign the 5 primary frequency signals from the private method to the five personality traits
        # openness, conscientiousness, extraversion, agreeableness, neuroticism
        
    def display_info(self):
        return f"{self.filepath}"

    # define a public method to visualize a waveform

    # define a private method to extract the 5 primary frequency signals from the waveform
