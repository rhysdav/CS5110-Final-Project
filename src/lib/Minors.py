class Minors:
    CONSTANTS = {
        'MATH': 'MATH',
        'BUSINESS': 'BUSINESS',
        'OTHER': 'OTHER'
    }

    def get(self, const_type):
        return self.CONSTANTS[const_type]
