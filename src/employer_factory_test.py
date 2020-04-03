from factory.EmployerFactory import EmployerFactory

def run_test_1():
    factory = EmployerFactory()
    test_employer = factory.generateEmployer('WEB_MOBILE')

    assert test_employer.employer_category == 'WEB_MOBILE'
    assert test_employer.preferred_gpa >= 2.0 and test_employer.preferred_gpa <= 4.0
    assert len(test_employer.preferred_skills) > 0
    assert test_employer.min_salary_offered >= 35000 and test_employer.min_salary <= 50000
    assert test_employer.preferred_degree_name is not None
    assert test_employer.preferred_minor_name == 'MATH'

    print("===== TEST EMPLOYER ====")
    print('category: {}'.format(test_employer.employer_category))
    print('Preferred GPA: {}'.format(test_employer.preferred_gpa))
    print('Preferred Skills: {}'.format(', '.join(test_employer.preferred_skills))
    print('Required Experience: {}'.format(test_employer.required_years_experience))
    print('Min Salaray Offered: {}'.format(test_employer.min_salary_offered))
    print('Preferred Degree: {}'.format(test_employer.preferred_degree_name))
    print('Preferred Minor: {}'. format(test_employer.preferred_minor_name))

def run_test_2():
    num_employers = 20
    factory = EmployerFactory()
    employers = factory.generateCandidates(num_employers)
    assert len(employers) == num_employers


if __name__ == '__main__':
    run_test_1()
    run_test_2()
