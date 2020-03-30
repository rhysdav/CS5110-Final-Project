class CandidateProject(object):
    def __init__(self, job_category, length_in_months, skills, project_type='school'):
        self.job_category = job_category
        self.length_in_months = length_in_months
        self.skills = skills
        self.project_type = project_type

    def set_job_category(self, category):
        self.job_category = category

    def set_length_in_months(self, length_in_months):
        self.length_in_months = length_in_months

    def set_skills(self, skills):
        self.skills = skills

    def project_type(self, project_type):
        self.project_type = project_type
