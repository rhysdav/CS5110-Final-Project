class JobCategories:
    CONSTANTS = {
        'WEB_MOBILE': 'WEB_MOBILE',
        'DATA_SCIENCE_ML': 'DATA_SCIENCE_ML',
        'EMBEDDED_SYSTEMS': 'EMBEDDED_SYSTEMS',
        'GAME_DEV': 'GAME_DEV',
    }

    def get(self, const_type):
        return self.CONSTANTS[const_type]
