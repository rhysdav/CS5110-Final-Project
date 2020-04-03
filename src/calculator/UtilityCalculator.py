import random

class UtilityCalculator(object):
    def __init__(self):
        super().__init__()
        random.seed()

    def calclulateCandidateBaseUtility(self, candidate):
        return random.random() * 10 # random utitlity for now from 0 to 10


    def calculateEmployerBaseUtility(self, employer):
        return random.random() * 10 # random utility for now from 0 to 10
