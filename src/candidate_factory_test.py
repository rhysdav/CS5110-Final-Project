from factory.CandidateFactory import CandidateFactory

def run_test_1():
    factory = CandidateFactory()
    test_candidate = factory.generateCandidate('WEB_MOBILE')

    assert test_candidate.preferred_category == 'WEB_MOBILE'
    assert len(test_candidate.courses) > 0
    assert test_candidate.gpa >= 2.0 and test_candidate.gpa <= 4.0
    assert len(test_candidate.skills) > 0
    assert 'Python' in test_candidate.skills

    if test_candidate.years_experience > 0:
        assert test_candidate.experience_category is not None

    assert test_candidate.min_salary >= 35000 and test_candidate.min_salary <= 50000
    assert test_candidate.degree_name is not None
    assert test_candidate.degree_level == 'BS'

    print("===== TEST CANDIDATE ====")
    print('category: {}'.format(test_candidate.preferred_category))
    print('gpa: {}'.format(test_candidate.gpa))
    print('skills: {}'.format(', '.join(test_candidate.skills)))
    print('years_experience: {}'.format(test_candidate.years_experience))
    print('experience_category: {}'.format(test_candidate.experience_category))
    print('min salary: {}'.format(test_candidate.min_salary))
    print('degree name: {}'.format(test_candidate.degree_name))

def run_test_2():
    num_candidates = 20
    factory = CandidateFactory()
    candidates = factory.generateCandidates(num_candidates)
    assert len(candidates) == num_candidates


if __name__ == '__main__':
    run_test_1()
    run_test_2()
