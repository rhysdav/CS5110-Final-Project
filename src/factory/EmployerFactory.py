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
            pull_2_top_k=random.randint(5,12),
            pull_3_top_k=random.randint(2,4),
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
            skills_pool = ['DevOps', 'C#', 'MySQL', 'Unit testing', 'PHP', 'Angular', 'TypeScript', 'Bootstrap', 'LESS', 'Postgres', 'MongoDB', 'JIRA', 'AWS', 'Ruby on Rails', 'Laravel', 'Symphony', 'Swift', 'ASP.NET', '.NET', 'Spring', 'jQuery', 'Node', 'Webpack', 'Yarn', 'ReactJS', 'AngularJS', 'JavaScript', 'Django', 'Python', 'Java', 'Agile', 'API', 'Cyber Security', 'Encryption', 'Authentication']
        elif 'DATA_SCIENCE_ML' == job_category:
            skills_pool = ['Big Data', 'Statistics', 'AWS', 'Hadoop', 'Storm', 'Hive', 'Spark', 'Node', 'Webpack', 'Yarn', 'MapReduce', 'ML', 'AI', 'Tableau', 'TensorFlow', 'Keras', 'Neural Networks', 'Python', 'Java']
        elif 'EMBEDDED_SYSTEMS' == job_category:
            skills_pool = ['C', 'C++', 'Assembly', 'Microcontrollers', 'Linux', 'Architecture', 'Embedded', 'Eclipse', 'State Machines', 'Kernel', 'RTOS', 'Parallelism']
        else:
            skills_pool = ['Unity', 'Maya', 'CryEngine', 'Unreal Engine', 'AI', 'Animation', 'Game Design', 'C++', 'C#', 'Gimp', 'Blender', 'Objective-C']

        num_skills = random.randint(3, 7)
        while len(add_skills) < num_skills:
            choice = random.choice(skills_pool)
            if choice not in add_skills:
                add_skills.append(choice)

        return add_skills

    def generateWeights(self):
        total_points = 50
        weight_attributes = ['preferred_candidate_category', 'min_gpa', 'required_years_experience', \
            'required_years_experience', 'preferred_skills', 'preferred_degree_name', 'preferred_minor_name', \
            'personality_score', 'projects', 'coding_exam']
        max_points = int(total_points/int(len(weight_attributes)/2))
        weights = {}
        for att in weight_attributes:
            if total_points > max_points:
                points = random.randrange(max_points+1)
            elif total_points > 0:
                points = random.randrange(total_points+1)
            else:
                points = 0
            weights[att] = points
            total_points -= points
        return weights
