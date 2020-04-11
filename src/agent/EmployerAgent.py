class EmployerAgent(object):
    '''Makes decisions on behalf of assigned agent.'''

    def __init__(self, employer):
        self.employer = employer

# init some resource in hrs spent
# each pull -= amount of resources
# after resources spent, may not have any candidates
