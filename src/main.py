from test.candidate_factory_test import run_all as candidate_factory_test
from test.employer_factory_test import run_all as employer_factory_test
from test.salary_negotiation_test import check_runs as salary_negotiation

def run_factory_tests():
    print('Running Candidate Factory test cases...')
    candidate_factory_test()

    print('\n\nRunning Employer Factory test cases...')
    employer_factory_test()

    print('Done.')

def run():
    pass

if __name__ == '__main__':
    run_factory_tests()
    # salary_negotiation()
