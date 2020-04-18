from random import randint

class CandidateAgent(object):
    '''Makes decisions on behalf of assigned candidate.'''

    def __init__(self, candidate):
        self.candidate = candidate
        self.num_applications = 1
        self.negotiation_resources = 100
        self.offers = [] # contains tuples with ($ offer amount, EmployerAgent)
        self.min_salary = candidate.min_salary
        self.current_highest_offer = 0
        self.initialize_resources()

    def initialize_resources(self):
        min_resources = 5.5 # min resources to complete one application from start to acceptance
        self.num_applications = randint(1,2)
        self.resources = min_resources * self.num_applications

    def has_resources(self, required_resources=0):
        return self.resources > required_resources

    def use_resources(self, resource_amount):
        if self.has_resources(resource_amount):
            resources = self.resources - resource_amount
            self.resources = resources
            return True
        return False

    def add_offer(self, offer):
        offers = self.offers
        offers.append(offer)
        self.offers = offers

    def reset_offers(self):
        # clears old offers
        self.offers = []

    def check_all_offers_equal(self):
        # checks if offers are equal and if so, returns offer with highest employer team score
        all_offers_are_equal = False
        check_amt = 0
        for offer in self.offers:
            if check_amt != 0 and offer[0] == check_amt:
                all_offers_are_equal = True
            else:
                all_offers_are_equal = False

        if all_offers_are_equal:
            offers = sorted(offers, key=lambda x: x[1].employer.team_score) #sort by team score
            return (True, offers[0])

        return False

    def consider_offers(self):
        if len(self.offers):
            offers = sorted(self.offers, key=lambda x: x[0]) #sort offers by amount

            if offers[0][0] >= self.min_salary and offers[0][0] == self.current_highest_offer:
                # candidate has already tried to get higher offer from higest offering employer but
                # employer was unwilling to go higher
                self.reset_offers()
                return (True, offers[0][0], offers[0][1])
            else:
                self.current_highest_offer = offers[0][0]

            if offers[-1][0] > self.min_salary:
                # update min salary to lowest offer (plus $1k so that lowest offer is not automatically accepted)
                self.min_salary = offers[-1][0] + 1000

            if self.use_resources(1):
                if offers[0][0] >= self.min_salary: # check highest offer is acceptable
                    top_offer_from_equal =  self.check_all_offers_equal()
                    self.reset_offers()
                    if top_offer_from_equal:
                        if randint(0,1): # if 0, candidate doesn't care about team score and will try to get a higher offer
                            return (True, top_offer_from_equal[0], top_offer_from_equal[1])
                    else:
                        if randint(0,1): # if 1, candidate will accept highest offer
                            return (True, offers[0][0], offers[0][1])
                        elif self.has_resources(1):
                            # gamble for higher offer
                            self.min_salary = offers[0][0]
                            return (False, offers)

                elif self.has_resources(1):
                    # All offers are too low
                    self.reset_offers()
                    return (False, offers)

        return (False, None)
