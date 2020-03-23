class Degrees:
    CONSTANTS = {
        'BACHELORS_CS': 'BACHELORS_CS',
        'MASTERS_CS': 'MASTERS_CS',
        'BACHELORS_CE': 'BACHELORS_CE',
        'MASTERS_CE': 'MASTERS_CE',
        'BACHELORS_MIS': 'BACHELORS_MIS'
    }

    def get(self, const_type):
        return self.CONSTANTS[const_type]
