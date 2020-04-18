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
        self.constants = dict(
            pull1_time_employer = 0.25, # 15 minutes
            pull1_time_candidate = 0.25,
            pull2_time_employer = 1, # 1 hour
            pull2_time_candidate = 2.75, # 2 hours 45 minutes
            pull3_time_employer = 5,
            pull3_time_candidate = 1.5
        )

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


    def sort_candidates(self, candidates):
        # sort candidate list according from highest utility to lowest
        candidates.sort(key=lambda candidate: candidate[0], reverse=True)
        return candidates


    def arm_pull_1(self):
        # Assign canidates to employer - application process - based on candidate category preferrence
        # Agent will pull highest canidates
        # costs 15min per candidate to employer
        categories = {}
        for employer in self.employers:
            categories[employer.employer.employer_category] = []

        for candidate in self.candidates:
            preferred_category = candidate.candidate.preferred_category
            if preferred_category in categories:
                categories[preferred_category].append([candidate.candidate.base_utility, candidate])
                candidate.use_resources(self.constants['pull1_time_candidate'] * sum([e.employer.employer_category == preferred_category for e in self.employers]))

        for category, c_list in categories.items():
            # sort candidate list according from highest utility to lowest
            c_list = self.sort_candidates(c_list)
            for employer in self.employers:
                if employer.employer.employer_category == category:
                    employer.set_candidates(c_list)
                    employer.use_resources(self.constants['pull1_time_employer'] * len(c_list))


    def arm_pull_2(self, k):
        # top k candidates to interview
        # each candidate interview requires 45min
        # first interview / coding exam
        # coding exam costs candidate 2hrs
        # cost employer 15min to review exam result
        # total cost employer: 1hr
        # total cost candidate: 2h 45m
        # personality_score
        for employer in self.employers:
            for candidate in employer.qualified_candidates:
                adjusted_utility = candidate[0]
                candidate[0] = self.utility_calculator.calculateInitialMatchUtility(employer.employer, candidate[1].candidate, adjusted_utility) # update adusted utility
                candidate[1].use_resources(self.constants['pull2_time_candidate'])
            candidates = employer.qualified_candidates.copy()
            candidates = self.sort_candidates(candidates)
            employer.set_candidates(candidates[:k])
            employer.use_resources(self.constants['pull2_time_employer'] * k)


    def arm_pull_3(self, k):
        # cost employer 5hrs
        # cost candidate 1.5h
        # meeting the team - team & personality_score
        for employer in self.employers:
            for candidate in employer.qualified_candidates:
                adjusted_utility = candidate[0]
                candidate[0] = self.utility_calculator.calculateFinalMatchUtility(employer.employer, candidate[1].candidate, adjusted_utility) # update adusted utility
                candidate[1].use_resources(self.constants['pull3_time_candidate'])
            candidates = employer.qualified_candidates.copy()
            candidates = self.sort_candidates(candidates)
            employer.set_candidates(candidates[:k])
            employer.use_resources(self.constants['pull3_time_employer'] * k)
            self.final_candidates.extend(candidates)


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
            for candidate in self.final_candidates:
                adjusted_utility, candidate_agent = candidate
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
