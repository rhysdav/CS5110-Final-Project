from factory.CandidateFactory import CandidateFactory

def run_test_1():
    factory = CandidateFactory()
    test_candidate = factory.generateCandidate()

    assert test_candidate.preferred_category is not None
    assert len(test_candidate.courses) > 0
    assert test_candidate.gpa >= 2.0 and test_candidate.gpa <= 4.0
    assert len(test_candidate.skills) > 0
    assert 'Python' in test_candidate.proficient_languages
    assert 'Agile' in test_candidate.skills

    if test_candidate.years_experience > 0:
        assert test_candidate.experience_category is not None

    if len(test_candidate.projects):
        for project in test_candidate.projects:
            assert project.length_in_months >= 1
            assert project.job_category is not None
            assert project.project_type is 'school' or project.project_type is 'personal'

    assert test_candidate.min_salary >= 35000 and test_candidate.min_salary <= 50000
    assert test_candidate.degree_name is not None
    assert test_candidate.degree_level == 'BS'

    print("===== TEST CANDIDATE ====")
    print('category: {}'.format(test_candidate.preferred_category))
    print('gpa: {}'.format(test_candidate.gpa))
    print('skills: {}'.format(', '.join(test_candidate.skills)))
    print('years_experience: {}'.format(test_candidate.years_experience))
    print('experience_category: {}'.format(test_candidate.experience_category))
    print('projects: {}'.format(len(test_candidate.projects)))
    if len(test_candidate.projects):
        for project in test_candidate.projects:
            print('----------------------')
            print('\tproject_category: {}'.format(project.job_category))
            print('\tproject_length: {} months'.format(project.length_in_months))
            print('\tproject_type: {}'.format(project.project_type))
    print('min salary: {}'.format(test_candidate.min_salary))
    print('degree name: {}'.format(test_candidate.degree_name))

def run_test_2():
    num_candidates = 20
    factory = CandidateFactory()
    candidates = factory.generateCandidates(num_candidates)
    assert len(candidates) == num_candidates

def run_all():
    run_test_1()
    run_test_2()
