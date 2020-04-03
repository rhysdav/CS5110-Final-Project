from factory.EmployerFactory import EmployerFactory

def run_test_1():
    factory = EmployerFactory()
    test_employer = factory.generateEmployer('GAME_DEV')

    assert test_employer.employer_category == 'GAME_DEV'
    assert test_employer.min_gpa >= 2.0 and test_employer.min_gpa <= 4.0
    assert len(test_employer.preferred_skills) > 0
    assert test_employer.min_salary_offered >= 35000 + test_employer.required_years_experience * 10000 and test_employer.min_salary_offered <= 50000  + test_employer.required_years_experience * 10000
    assert test_employer.preferred_degree_name is not None
    assert test_employer.preferred_minor_name == 'MATH'

    print("===== TEST EMPLOYER =====")
    print('category: {}'.format(test_employer.employer_category))
    print('Min GPA: {}'.format(test_employer.min_gpa))
    print('Preferred Skills: {}'.format(', '.join(test_employer.preferred_skills)))
    print('Required Experience: {}'.format(test_employer.required_years_experience))
    print('Min Salaray Offered: {}'.format(test_employer.min_salary_offered))
    print('Preferred Degree: {}'.format(test_employer.preferred_degree_name))
    print('Preferred Minor: {}'. format(test_employer.preferred_minor_name))
    print("=========================")

def run_test_2():
    num_employers = 20
    factory = EmployerFactory()
    employers = factory.generateEmployers(num_employers)
    assert len(employers) == num_employers


if __name__ == '__main__':
    run_test_1()
    run_test_2()
