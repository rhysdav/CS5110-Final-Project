from random import randint
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
            employer_agents.append(EmployerAgent(employer))

        self.employers = employer_agents


        candidate_agents = []
        for i in range(num_candidates):
            candidate = self.candidate_factory.generateCandidate()
            candidate.set_base_utility(self.utility_calculator.calclulateCandidateBaseUtility(candidate))
            candidate_agents.append(CandidateAgent(candidate))

        self.candidates = candidate_agents


    def sort_candidates(self, candidates):
        # sort candidate list according from highest utility to lowest
        candidates.sort(key=lambda candidate: candidate[0], reverse=True)
        return candidates


    def arm_pull_1(self):
        # Assign canidates to employer - application process - based on candidate category preferrence
        # Agent will pull highest canidates
        categories = {}
        for employer in self.employers:
            categories[employer.employer.employer_category] = []

        for candidate in self.candidates:
            preferred_category = candidate.candidate.preferred_category
            if preferred_category in categories:
                categories[preferred_category].append([candidate.candidate.base_utility, candidate])

        for category, c_list in categories.items():
            # sort candidate list according from highest utility to lowest
            for employer in self.employers:
                emp_c_list = []

                for candidate in c_list:
                    if randint(0,1): #simulates candidate choosing to apply for job
                        emp_c_list.append(candidate)

                emp_c_list = self.sort_candidates(emp_c_list)
                if employer.employer.employer_category == category:
                    employer.set_candidates(emp_c_list)


    def arm_pull_2(self, k=5):
        # top k candidates to interview
        # first interview - employer weights applied to candidate traits
        for employer in self.employers:
            if not k:
                k = employer.employer.pull_2_top_k

            for candidate in employer.qualified_candidates:
                candidate[0] = self.utility_calculator.calculateInitialMatchUtility(employer.employer, candidate[1].candidate) # update adusted utility
            candidates = employer.qualified_candidates.copy()
            candidates = self.sort_candidates(candidates)
            employer.set_candidates(candidates[:k])


    def arm_pull_3(self, k=3):
        # second interview 
        # coding exam, personality_score
        for employer in self.employers:
            if not k:
                k = employer.employer.pull_3_top_k

            for candidate in employer.qualified_candidates:
                candidate[0] = self.utility_calculator.calculateFinalMatchUtility(employer.employer, candidate[1].candidate) # update adusted utility
            candidates = employer.qualified_candidates.copy()
            candidates = self.sort_candidates(candidates)[:k]
            employer.set_candidates(candidates)
            for c in candidates:
                if c[1] not in self.final_candidates:
                    self.final_candidates.append(c[1])


    def salary_negotiation(self):
        employers_done = []
        candidates_done = []

        while len(self.employer_candidate_matches) < len(self.employers):
            # employer offer round
            for employer_agent in self.employers:
                if employer_agent.employer.uuid not in employers_done:
                    offer = employer_agent.extend_offer()
                    candidate_agent = employer_agent.top_candidate

                    while (candidate_agent.candidate.uuid in candidates_done and offer):
                        offer = employer_agent.extend_offer(get_next_top_candidate=True)
                        if offer:
                            candidate_agent = offer[0]
                        else:
                            break

                    if offer:
                        candidate_agent.add_offer(offer[1])
                    else:
                        employers_done.append(employer_agent.employer.uuid)
                        self.employer_candidate_matches.append((False, employer_agent.employer, False))

            # candidate acceptance round
            for candidate_agent in self.final_candidates:
                if candidate_agent not in candidates_done:
                    if len(candidate_agent.offers): # candidate may not have offers on first round, but receive offers later
                        accepted = candidate_agent.consider_offers()
                        if accepted[0]:
                            accepted_flag, offer_amount, employer_agent = accepted
                            self.employer_candidate_matches.append((candidate_agent.candidate, employer_agent.employer, offer_amount))
                            employers_done.append(employer_agent.employer.uuid)
                            candidates_done.append(candidate_agent.candidate.uuid)
                        else:
                            offers = accepted[1]
                            if offers is not None:
                                for offer in offers:
                                    # tell employer offer is too low
                                    offer[1].offer_is_too_low = True
