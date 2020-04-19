from agent.CentralAgent import CentralAgent


def print_employer(employer):
    print('Employer ID: {}'.format(employer.employer.uuid))
    print('Employer category: {}'.format(employer.employer.employer_category))
    print('Preferred skills: {}'.format(', '.join(employer.employer.preferred_skills)))
    print('Number of applicants: {}'.format(len(employer.qualified_candidates)))
    print('Remaining resources: {}'.format(employer.resources))


def print_candidate(candidate, salary):
    print('\nCandidate ID: {}'.format(candidate.uuid))
    print('Candidate category: {}'.format(candidate.preferred_category))
    print('Accepted Salary: ${}'.format(salary))
    print('Languages: {}'.format(candidate.proficient_languages))
    print('Skills: {}'.format(candidate.skills))
    print('Years experience: {}'.format(candidate.years_experience))
    print('Experience Category: {}'.format(candidate.experience_category))
    print('Number of projects: {}'.format(len(candidate.projects)))
    print('Base utility: {}'.format(candidate.base_utility))
    print('GPA: {}'.format(candidate.gpa))

def print_employer_summary(employers):
    for e in employers:
        print_employer(e)
        print('Applicants:')
        for c in e.qualified_candidates:
            print_candidate(c[1].candidate)


def print_final_results(matches, num_employers=8, num_candidates=100, include_employer_summary=False, include_unfilled_summary=False, include_candidate_summary=False):
    print('\nFinal Results')
    cnt_matches = 0
    cnt_failures = 0
    unfilled = []
    for m in matches:
        if m[0]:
            if include_employer_summary:
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

    if include_unfilled_summary:
        print('\nUnfilled Positions:')
        categories = {}
        for u in unfilled:
            if u.employer_category in categories.keys():
                categories[u.employer_category] += 1
            else:
                categories[u.employer_category] = 1
            print('Job Category: {}'.format(u.employer_category))
            print('Employer ID: {}'.format(u.uuid))
            print('Allowed Salary range: ${} - ${}'.format(u.min_salary_offered, u.max_salary_offered))
        print (categories)

    if include_candidate_summary:
        candidates=[]
        for m in matches:
            if m[0] is not False:
                print_candidate(m[0], m[2])
                candidates.append(m[0])
        return candidates


def compute_avgs(matched_candidates, all_candidates):
    print('\nAverage utilities of unhired candidates by category:')
    categories = {}
    for c in all_candidates:
        candidate = c.candidate
        if candidate not in matched_candidates:
            if candidate.preferred_category in categories.keys():
                categories[candidate.preferred_category].append(candidate)
                categories[candidate.preferred_category + '_UTILITY'] += candidate.base_utility
            else:
                categories[candidate.preferred_category] = [candidate]
                categories[candidate.preferred_category + '_UTILITY'] = candidate.base_utility

    for k in categories.keys():
        if '_UTILITY' in k:
            continue
        else:
            print('{}: {}'.format(k, categories[k+'_UTILITY']/len(categories[k])))
            

def run_test_1():
    print('\n\n')
    print('=============== Central Agent Test #1 ===============')
    central_agent = CentralAgent()
    num_employers=100
    num_candidates=100
    central_agent.initialize(num_employers=num_employers, num_candidates=num_candidates)

    # assert len(central_agent.candidates) == 100
    # assert len(central_agent.employers) == 8
    print('Central agent initialization successful')
    print('Initialized Employers:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_1()
    print('\nArm pull 1 successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_2(k=12)
    print('\nArm pull 2 successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.arm_pull_3(k=3)
    print('\nArm pull 3 successful')
    print('Results:')
    # print_employer_summary(central_agent.employers)

    central_agent.salary_negotiation()
    print('Salary negotiation successful')
    print_final_results(central_agent.employer_candidate_matches, num_employers, num_candidates)
    # print_employer_summary(central_agent.employers)

    print('Done.')


def run_test_2():
    print('\n\n')
    print('=============== Central Agent Test #2 - Candidate Comparison ===============')
    central_agent = CentralAgent()
    num_employers=5
    num_candidates=100
    central_agent.initialize(num_employers=num_employers, num_candidates=num_candidates)

    assert len(central_agent.candidates) == num_candidates
    assert len(central_agent.employers) == num_employers

    print('Central agent initialization successful')

    central_agent.arm_pull_1()
    print('\nArm pull 1 successful')

    central_agent.arm_pull_2(k=3)
    print('\nArm pull 2 successful')

    central_agent.arm_pull_3(k=1)
    print('\nArm pull 3 successful')

    central_agent.salary_negotiation()
    print('Salary negotiation successful')
    matched_candidates = print_final_results(
        matches=central_agent.employer_candidate_matches,
        num_employers=num_employers,
        num_candidates=num_candidates,
        include_candidate_summary=True)

    compute_avgs(matched_candidates, central_agent.candidates)

    print('Done.')

def run_all():
    # run_test_1()
    run_test_2()
