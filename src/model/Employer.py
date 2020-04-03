class Employer(object):
    def __init__(self,
        employer_category,
        preferred_candidate_category,
        preferred_degree_level,
        preferred_degree_name,
        preferred_minor_name,
        required_years_experience,
        preferred_languages,
        preferred_frameworks,
        min_salary_offered):
        self.employer_category = employer_category
        self.preferred_candidate_category = preferred_candidate_category
        self.preferred_degree_level = preferred_degree_level
        self.preferred_degree_name = preferred_degree_name
        self.preferred_minor_name = preferred_minor_name
        self.required_years_experience = required_years_experience
        self.preferred_languages = preferred_languages
        self.preferred_frameworks = preferred_frameworks
        self.min_salary_offered = min_salary_offered

    def set_employer_category(self, category):
        self.employer_category = category

    def set_preferred_candidate_category(self, category):
        self.preferred_candidate_category = category

    def set_preferred_degree_level(self, level):
        self.preferred_degree_level = level

    def set_preferred_degree_name(self, name):
        self.preferred_degree_name = name

    def set_preferred_minor_name(self, name):
        self.preferred_minor_name = name

    def set_required_years_experience(self, years):
        self.required_years_experience = years

    def set_preferred_languages(self, languages):
        self.preferred_languages = languages

    def add_preferred_language(self, language):
        languages = self.preferred_languages
        languages.append(language)
        self.preferred_languages = languages

    def set_preferred_frameworks(self, frameworks):
        self.preferred_frameworks = frameworks

    def add_preferred_frameworks(self, framework):
        frameworks = self.preferred_frameworks
        frameworks.append(framework)
        self.preferred_frameworks = frameworks

    def set_min_salary_offered(self, salary):
        self.min_salary_offered = salary




