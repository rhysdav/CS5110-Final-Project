from random import randrange

class EmployerAgent(object):
    '''Makes decisions on behalf of assigned agent.'''

    def __init__(self, employer):
        self.employer = employer
        self.resources = 7
        self.qualified_candidates = [] # array of candidate agents
        self.top_candidate = None
        self.current_offer = self.employer.min_salary_offered
        self.offer_is_too_low = False

    def has_resources(self, required_resources=0):
        return self.resources > required_resources

    def use_resources(self, resource_amount):
        if self.has_resources(resource_amount):
            resources = self.resources - resource_amount
            self.resources = resources
            return True
        return False

    def set_top_candidate(self):
        qualified_candidates = self.qualified_candidates
        if len(qualified_candidates):
            self.top_candidate = qualified_candidates.pop(0)
            self.qualified_candidates = qualified_candidates
            return candidate
        else:
            self.top_candidate = None

        return False

    def extend_offer(self, offer_was_low=False, get_next_top_candidate=False):
        candidate = self.top_candidate

        if candidate is None or get_next_top_candidate:
            self.set_top_candidate
            candidate = self.top_candidate

        if candidate and candidate.min_salary <= self.employer.max_salary_offered:
            if self.offer_is_too_low:
                self.current_offer = min(self.current_offer + randrange(2000, 5000, 1000), candidate.min_salary)
            else:
                self.current_offer = candidate.min_salary

            if self.use_resources(0.75):
                return (candidate, (self.current_offer, self))

        return False


# init some resource in hrs spent
# each pull -= amount of resources
# after resources spent, may not have any candidates
