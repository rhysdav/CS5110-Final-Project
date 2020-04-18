from agent.CentralAgent import CentralAgent


def print_employer(employer):
    print('Employer category: {}'.format(employer.employer.employer_category))
    print('Preferred skills: {}'.format(', '.join(employer.employer.preferred_skills)))
    print('Number of applicants: {}'.format(len(employer.qualified_candidates)))
    print('Remaining resources: {}'.format(employer.resources))


def print_candidate(candidate):
    print('Candidate category: {}'.format(candidate.preferred_category))
    print('Languages: {}'.format(candidate.proficient_languages))
    print('Skills: {}'.format(candidate.skills))
    print('Years experience: {}'.format(candidate.years_experience))
    print('Number of projects: {}'.format(len(candidate.projects)))
    print('Base utility: {}'.format(candidate.base_utility))


def print_employer_summary(employers):
    for e in employers:
        print_employer(e)
        # print('Applicants:')
        # for c in e.qualified_candidates:
        #     print_candidate(c.candidate)


def run_test_1():
    print('\n\n')
    print('=============== Central Agent Test #1 ===============')
    central_agent = CentralAgent()
    central_agent.initialize()

    assert len(central_agent.candidates) == 100
    assert len(central_agent.employers) == 8
    print('Central agent initialization successful')
    print('Initialized Employers:')
    print_employer_summary(central_agent.employers)

    central_agent.arm_pull_1()
    print('\nArm pull 1 successful')
    print('Results:')
    print_employer_summary(central_agent.employers)

    central_agent.arm_pull_2(5)
    print('\nArm pull 2 (with k = 5) successful')
    print('Results:')
    print_employer_summary(central_agent.employers)

    central_agent.arm_pull_3(3)
    print('\nArm pull 3 (with k = 3) successful')
    print('Results:')
    print_employer_summary(central_agent.employers)

    central_agent.salary_negotiation()
    print('Salary negotiation successful')

    print('Done.')


def run_all():
    run_test_1()
