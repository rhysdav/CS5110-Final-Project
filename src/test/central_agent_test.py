from agent.CentralAgent import CentralAgent


def print_employer(employer):
    print('Employer ID: {}'.format(employer.employer.uuid))
    print('Employer category: {}'.format(employer.employer.employer_category))
    print('Preferred skills: {}'.format(', '.join(employer.employer.preferred_skills)))
    print('Number of applicants: {}'.format(len(employer.qualified_candidates)))
    print('Remaining resources: {}'.format(employer.resources))


def print_candidate(candidate):
    print('Candidate ID: {}'.format(candidate.uuid))
    print('Candidate category: {}'.format(candidate.preferred_category))
    # print('Languages: {}'.format(candidate.proficient_languages))
    # print('Skills: {}'.format(candidate.skills))
    # print('Years experience: {}'.format(candidate.years_experience))
    # print('Number of projects: {}'.format(len(candidate.projects)))
    # print('Base utility: {}'.format(candidate.base_utility))


def print_employer_summary(employers):
    for e in employers:
        print_employer(e)
        print('Applicants:')
        for c in e.qualified_candidates:
            print_candidate(c[1].candidate)


def print_final_results(matches, num_employers=8, num_candidates=100):
    print('\nFinal Results')
    cnt_matches = 0
    cnt_failures = 0
    unfilled = []
    for m in matches:
        if m[0]:
            print('Job Category: {}'.format(m[1].employer_category))
            print('Accepted offer amount: ${}'.format(m[2]))
            print('Candidate Negotiated for Higher Salary: {}'.format('Yes' if m[2] != m[1].min_salary_offered else 'No'))
            print('Employer ID: {}'.format(m[1].uuid))
            print('Candidate ID: {}\n'.format(m[0].uuid))
            cnt_matches += 1
        else:
            unfilled.append(m[1])
            cnt_failures += 1

    print('# Employers: {}'.format(num_employers))
    print('# Total Candidates in Pool: {}'.format(num_candidates))
    print('Total filled postions: {}'.format(cnt_matches))
    print('Total unfilled postions: {}'.format(cnt_failures))
    print('\nUnfilled Positions:')

    # for u in unfilled:
    #     print('Job Category: {}'.format(u.employer_category))
    #     print('Employer ID: {}'.format(u.uuid))
    #     print('Allowed Salary range: ${} - ${}'.format(u.min_salary_offered, u.max_salary_offered))


def run_test_1():
    print('\n\n')
    print('=============== Central Agent Test #1 ===============')
    central_agent = CentralAgent()
    central_agent.initialize(num_employers=1000, num_candidates=100)

    # assert len(central_agent.candidates) == 100
    # assert len(central_agent.employers) == 8
    print('Central agent initialization successful')
    print('Initialized Employers:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_1()
    print('\nArm pull 1 successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_2(5)
    print('\nArm pull 2 (with k = 5) successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_3(3)
    print('\nArm pull 3 (with k = 3) successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.salary_negotiation()
    print('Salary negotiation successful')
    print_final_results(central_agent.employer_candidate_matches, num_employers=len(central_agent.employers), num_candidates=len(central_agent.candidates))

    # print_employer_summary(central_agent.employers)

    print('Done.')



def run_all():
    run_test_1()
