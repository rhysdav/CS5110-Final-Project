import random
from uuid import uuid4
from model.Employer import Employer
from lib.JobCategories import JobCategories
from lib.Degrees import Degrees
from lib.Minors import Minors
from calculator.UtilityCalculator import UtilityCalculator


class EmployerFactory(object):
    """
    Generates Employer criteria.

    -------- NOTES --------
    employer category == preferred candidate category?

    SALARY
        * Should employers have a max salary?
        * min salary offered goes up $10,000 for each one year of experience

    SKILLS
        * Preferred skills generated for an employer are the same for candidates currently
        * those skills could have weights assigned to them, signifying which skills are desired

    DEGREE & MINOR
        * How should minors and degrees be determined?

    GPA
        * min accepted GPA is random between 2.0 and 4.0
        * should there even be a GPA associated with Employer?

    WEIGHTING


    """

    def __init__(self):
        super(EmployerFactory, self).__init__()
        random.seed()

    def generateEmployer(self, job_category):
        employer_category = JobCategories.get(JobCategories, const_type=job_category)
        preferred_candidate_category = JobCategories.get(JobCategories, const_type=job_category)

        required_years_experience = random.randint(0, 5)

        base = 35000
        increase = 35000 + (required_years_experience if required_years_experience else 1 * 1000)

        if employer_category == 'DATA_SCIENCE_ML':
            increase += random.randrange(5000, 10000, 1000)
        if employer_category == 'GAME_DEV':
            base -= random.randrange(3000, 5000, 1000)

        min_salary_offered = random.randrange(35000, increase, 1000)
        max_salary_offered = random.randrange(increase, 75000, 3000)

        min_gpa = round(random.randrange(2.0, 4.0) + random.random(), 2)

        preferred_skills = self.generateSkillsNeeded(employer_category)

        minor_name = Minors.get(Minors, const_type='MATH')
        degree_name = Degrees.get(Degrees, const_type='BACHELORS_CS')

        weights = self.generateWeights()

        employer = Employer(
            uuid=uuid4(),
            base_utility=0.0,
            employer_category=employer_category,
            preferred_candidate_category=preferred_candidate_category,
            min_salary_offered=min_salary_offered,
            min_gpa=min_gpa,
            required_years_experience=required_years_experience,
            preferred_skills=preferred_skills,
            max_salary_offered=max_salary_offered,
            team_score=random.randint(1,10),
            weights=weights,
            preferred_degree_name=degree_name,
            preferred_minor_name=minor_name
        )

        return employer

    def generateEmployers(self, num_employers, categories={'WEB_MOBILE': 0.45, 'DATA_SCIENCE_ML': 0.3, 'EMBEDDED_SYSTEMS': 0.1, 'GAME_DEV': 0.15}):
        employers = []

        for category, percent in categories.items():
            for _ in range(int(num_employers * percent)):
                employers.append(self.generateEmployer(category))

        while len(employers) < num_employers:
            employers.append(self.generateEmployer('WEB_MOBILE'))

        return employers


    def generateSkillsNeeded(self, job_category):
        add_skills = []
        skills_pool = []

        if 'WEB_MOBILE' == job_category:
            skills_pool = ['DevOps', 'C#', 'MySQL', 'Unit testing', 'PHP', 'Angular', 'TypeScript', 'Bootstrap', 'LESS', 'Postgres', 'MongoDB', 'JIRA', 'AWS', 'Ruby on Rails', 'Laravel', 'Symphony', 'Swift', 'ASP.NET', '.NET', 'Spring', 'jQuery', 'Node', 'Webpack', 'Yarn']
        elif 'DATA_SCIENCE_ML' == job_category:
            skills_pool = ['Big Data', 'Statistics', 'AWS', 'Hadoop', 'Storm', 'Hive', 'Spark', 'Node', 'Webpack', 'Yarn', 'MapReduce', 'ML', 'AI', 'Tableau', 'TensorFlow', 'Keras', 'Neural Networks']
        elif 'EMBEDDED_SYSTEMS' == job_category:
            skills_pool = ['C', 'C++', 'Assembly', 'Microcontrollers', 'Linux', 'Architecture', 'Embedded', 'Eclipse', 'State Machines', 'Kernel', 'RTOS']
        else:
            skills_pool = ['Unity', 'Maya', 'CryEngine', 'Unreal Engine', 'AI', 'Animation', 'Game Design', 'C++', 'C#', 'Gimp', 'Blender', 'Objective-C']

        num_skills = random.randint(3, 7)
        while len(add_skills) < num_skills:
            choice = random.choice(skills_pool)
            if choice not in add_skills:
                add_skills.append(choice)

        return add_skills

    def generateWeights(self):
        max_weight = 5.0
        weights = {}
        weights['preferred_candidate_category'] = random.uniform(max_weight*0.4, max_weight)
        weights['min_gpa'] = random.uniform(max_weight*0.1, max_weight*0.5)
        weights['required_years_experience'] = random.uniform(max_weight*0.5, max_weight)
        weights['preferred_skills'] = random.uniform(max_weight*0.3, max_weight)
        weights['preferred_degree_name'] = random.uniform(max_weight*0.5, max_weight)
        weights['preferred_minor_name'] = random.uniform(max_weight*0.2, max_weight*0.6)
        weights['personality_score'] = random.uniform(0, max_weight)
        weights['projects'] = random.uniform(0.5*max_weight, max_weight)
        weights['coding_exam'] = random.uniform(0.2*max_weight, max_weight)
        return weights
