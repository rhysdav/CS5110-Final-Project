import random
from model.Employer import Employer
from lib.JobCategories import JobCategories
from lib.Degrees import Degrees
from lib.Minors import Minors
from calculator.UtilityCalculator import UtilityCalculator


class CandidateFactory(object):
    """Generates Employer criteria."""

    def __init__(self):
        super(EmployerFactory, self).__init__()
        random.seed()

    def generateEmployer(self, job_category):
        employer_category = JobCategories.get(JobCategories, const_type=job_category)
        preferred_candidate_category = JobCategories.get(JobCategories, const_type=job_category)

        required_years_experience = random.randint(0, 4)
        preferred_skills = self.generateSkillsNeeded(self, employer_category)

        minor_name = Minors.get(Minors, const_type='MATH')
        degree_name = Degrees.get(Degrees, const_type='BACHELOR_CS')



        employer = Employer(
            base_utility=0.0,
            employer_category=employer_category,
            preferred_candidate_category=preferred_candidate_category,
            min_salary_offered=random.randrange(35000, 50000, 3000),
            preferred_gpa=round(random.randrange(2.0, 4.0) + random.random(), 2),
            required_years_experience=required_years_experience,
            preferred_skils=preferred_skills,
            preferred_degree_name=degree_name,
            preferred_minor_name=minor_name
        )

        calculator = UtilityCalculator()
        employer.set_base_utility(calculator.calclulateCandidateBaseUtility(employer))

        return employer

    def generateEmployers(self, num_employers, categories={'WEB_MOBILE': 0.6, 'DATA_SCIENCE_ML': 0.2, 'EMBEDDED_SYSTEMS': 0.1, 'GAME_DEV': 0.1}):
        employers = []

        for category, percent in categories.items():
            for _ in range(int(num_employers * percent)):
                employers.append(self.generateEmployer(category))

        while len(employers) < num_employers:
            employers.append(self.generateEmployer('WEB_MOBILE'))

        return candidates


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

        num_skills = random.randint(3,7)
        while len(add_skills) < num_skills:
            choice = random.choice(skills_pool)
            if choice not in add_skills:
                add_skills.append(choice)

        return add_skills
