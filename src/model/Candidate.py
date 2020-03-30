class Candidate(object):
    def __init__(self,
        base_utility,
        preferred_category,
        courses,
        gpa,
        proficient_languages,
        skills,
        years_experience,
        experience_category,
        projects,
        min_salary,
        personality_score,
        degree_name=None,
        minor_name=None,
        degree_level='BS'):
        self.base_utility = base_utility
        self.preferred_category = preferred_category
        self.courses = courses
        self.gpa = gpa
        self.proficient_languages = proficient_languages
        self.skills = skills
        self.years_experience = years_experience
        self.experience_category = experience_category
        self.projects = projects
        self.min_salary = min_salary
        self.personality_score = personality_score
        self.degree_name = degree_name
        self.minor_name = minor_name
        self.degree_level = degree_level

    def set_base_utility(self, base_utility):
        self.base_utility = base_utility

    def set_preferred_category(self, preferred_category):
        self.preferred_category = preferred_category

    def set_courses(self, courses):
        self.courses = courses

    def add_course(self, course):
        courses = self.courses
        courses.append(course)
        self.courses = courses

    def set_gpa(self, gpa):
        self.gpa = gpa

    def set_proficient_languages(self, proficient_languages):
        self.proficient_languages = proficient_languages

    def set_skills(self, skills):
        self.skills = skills

    def add_skill(self, skill):
        skills = self.skills
        skills.append(skill)
        self.skills = skillls

    def set_years_experience(self, years_experience):
        self.years_experience = years_experience

    def set_experience_category(self, experience_category):
        self.experience_category = experience_category

    def set_projects(self, projects):
        self.projects = projects

    def add_project(self, project):
        projects = self.projects
        projects.append(project)
        self.projects = projects

    def set_min_salary(self, min_salary):
        self.min_salary = min_salary

    def set_degree_name(self, degree_name):
        self.degree_name = degree_name

    def set_minor_name(self, minor_name):
        self.minor_name = minor_name

    def set_degree_level(self, degree_level):
        self.degree_level = degree_level
