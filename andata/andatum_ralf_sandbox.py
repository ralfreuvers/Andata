class andatum:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        # load song file into self and store the total waveform

        # randomly assign the 5 primary frequency signals from the private method to the five personality traits
        #                     <---low values--->                  <---high values--->
        # openness:             mono                                stereo
        # conscientiousness:    low compression                     high compression 
        # extraversion:         only low/mid freq                   open to all freq       
        # agreeableness:        hard compr+high freq spikes         (soft compr +) smooth eq
        # neuroticism:          normal                              pitch modulation + glitchy distortions
        
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    # define a public method to visualize a waveform

    # define a private method to extract the 5 primary frequency signals from the waveform
