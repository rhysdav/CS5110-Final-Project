from factory.CandidateFactory import CandidateFactory
from factory.EmployerFactory import EmployerFactory
from calculator.UtilityCalculator import UtilityCalculator
from agent.CandidateAgent import CandidateAgent
from agent.EmployerAgent import EmployerAgent

class CentralAgent(object):
    def __init__(self, candidates=[], employers=[]):
        self.candidates = candidates
        self.employers = employers
        self.candidate_factory = CandidateFactory()
        self.employer_factory = EmployerFactory()
        self.utility_calculator = UtilityCalculator()
        self.final_candidates = [] # candidates in employer qualified_candidates
        self.employer_candidate_matches = [] # final results

    def initialize(self, num_employers=8, num_candidates=100):
        employers = self.employer_factory.generateEmployers(num_employers)
        employer_agents = []
        for employer in employers:
            # add employer utility if needed
            employer_agents.append(EmployerAgent(employer))

        self.employers = employer_agents


        candidate_agents = []
        for i in range(num_candidates):
            candidate = self.candidate_factory.generateCandidate()
            candidate.set_base_utility(self.utility_calculator.calclulateCandidateBaseUtility(candidate))
            candidate_agents.append(CandidateAgent(candidate))

        self.candidates = candidate_agents


    def arm_pull_1(self):
        # Assign canidates to employer - application process - based on candidate category preferrence
        # Agent will pull highest canidates
        # costs 15min per candidate
        pass


    def arm_pull_2(self):
        # top k candidates to interview
        # each candidate interview requires 45min
        # first interview / coding exam
        # coding exam costs candidate 2hrs
        # cost employer 15min to review exam result
        # total cost employer: 1hr
        # total cost candidate: 2h 45m
        # personality_score
        pass


    def arm_pull_3(self):
        # cost employer 5hrs
        # cost candidate 1.5h
        # meeting the team - team & personality_score
        pass


    def salary_negotiation(self):
        employers_done = []
        candidates_done = []

        while len(employers_done) < len(self.employers):
            # employer offer round
            for employer_agent in self.employers:
                if employer_agent not in employers_done:
                    offer = employer_agent.extend_offer()
                    candidate_agent = employer_agent.top_candidate

                    while candidate_agent in candidates_done and offer:
                        offer = employer_agent.extend_offer(get_next_top_candidate=True)
                        candidate_agent = offer[0]

                    if offer:
                        candidate_agent.add_offer(offer[1])
                    else:
                        employers_done.append(employer_agent)

            # candidate acceptance round
            for candidate_agent in self.final_candidates:
                if candidate_agent in candidates_done:
                    self.final_candidates.remove(candidate_agent)
                else:
                    if len(candidate_agent.offers): # candidate may not have offers on first round, but receive offers later
                        accepted = candidate_agent.consider_offers()
                        if accepted[0]:
                            accepted_flag, offer_amount, employer_agent = accepted
                            self.employer_candidate_matches.append((candidate_agent.candidate, employer_agent.employer, offer_amount))
                            employers_done.append(employer_agent)
                            candidates_done.append(candidate_agent)
                            self.final_candidates.remove(candidate_agent)
                        else:
                            offers = accepted[1]
                            for offer in offers:
                                # tell employer offer is too low
                                offer[1].offer_is_too_low = True
