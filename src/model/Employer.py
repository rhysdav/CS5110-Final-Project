class Employer(object):
    def __init__(self,
        base_utility,
        employer_category,
        preferred_candidate_category,
        min_salary_offered,
        min_gpa,
        required_years_experience,
        preferred_skils,
        weights,
        preferred_degree_name=None,
        preferred_minor_name=None):
        self.base_utility = base_utility
        self.employer_category = employer_category
        self.preferred_candidate_category = preferred_candidate_category
        self.preferred_degree_name = preferred_degree_name
        self.preferred_minor_name = preferred_minor_name
        self.min_gpa = min_gpa
        self.required_years_experience = required_years_experience
        self.preferred_skills = preferred_skils
        self.min_salary_offered = min_salary_offered
        self.weights = weights

    def set_base_utility(self, base_utility):
        self.base_utility = base_utility

    def set_employer_category(self, category):
        self.employer_category = category

    def set_preferred_candidate_category(self, category):
        self.preferred_candidate_category = category

    def set_preferred_degree_name(self, name):
        self.preferred_degree_name = name

    def set_preferred_minor_name(self, name):
        self.preferred_minor_name = name

    def set_min_gpa(self, gpa):
        self.min_gpa = gpa

    def set_required_years_experience(self, years):
        self.required_years_experience = years

    def set_preferred_skills(self, skills):
        self.preferred_skills = skills

    def add_preferred_skill(self, skill):
        skills = self.preferred_skills
        skills.append(skill)
        self.preferred_skills = skills

    def set_min_salary_offered(self, salary):
        self.min_salary_offered = salary

    def set_weight(self, name, weight):
        self.weights[name] = weight




