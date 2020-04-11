from factory.CandidateFactory import CandidateFactory
from factory.EmployerFactory import EmployerFactory
from calculator.UtilityCalculator import UtilityCalculator

class CentralAgent(object):
    def __init__(self, candidates=[], employers=[]):
        self.candidates = candidates
        self.employers = employers
        self.candidate_factory = CandidateFactory()
        self.employer_factory = EmployerFactory()
        self.utility_calculator = UtilityCalculator()

    def initialize(num_employers=8, num_candidates=100):
        employers = self.employer_factory.generateEmployers(num_employers)
        # add employer utility if needed

        candidates = []
        for i in num_candidates:
            candidate = self.candidate_factory.generateCandidate()
            candidate.set_base_utility(self.utility_calculator.calclulateCandidateBaseUtility(candidate))
            candidates.append(candidate)

        self.candidates = candidates

    def arm_pull_1():
        # Assign canidates to employer - application process - based on candidate category preferrence
        # Agent will pull highest canidates
        # costs 15min per candidate
        pass

    def arm_pull_2():
        # top k candidates to interview
        # each candidate interview requires 45min
        # first interview / coding exam
        # coding exam costs candidate 2hrs
        # cost employer 15min to review exam result
        # total cost employer: 1hr
        # total cost candidate: 2h 45m
        # personality_score
        pass

    def arm_pull_3():
        # cost employer 5hrs
        # cost candidate 1.5h
        # meeting the team - team & personality_score
        pass

    def offer_acceptance():
        # costs employer per offer extended 45min
        # costs candidate 1hr per offer candidate has

        # salary negotiation:
        # candidate will attempt to negotiate if has multiple offers and remaining resources
        # employer will negotiate with candidate if has remaining resources else will
        # extend offer to runner up candidate
        # negotiation continues with runner ups
        # both candidate and employer may not find matches.
        pass
