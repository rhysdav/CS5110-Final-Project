import random

class UtilityCalculator(object):
	def __init__(self):
		super().__init__()
		random.seed()
		self.valuable_quality = 2
		self.standard_quality = 1
		self.gpa_scale_constant = 1/4
		self.max_candidate_ut = 54  # To find this maximum, I generated 1000 random candidates and this was the max utility I got
		self.max_employer_ut = 20

  #   def normalizedUtility(self, ut, max_ut):
  #   	# Returns the normalized utility for a candidate given the maximum
		# return (ut/max_ut)*10

	def calclulateCandidateBaseUtility(self, candidate):
		utility = 0

		# Calculate utility for projects
		for project in candidate.projects:
			utility += (project.length_in_months / 12) * len(project.skills)

		# Add utility for known languages and skills
		utility += len(candidate.proficient_languages) * self.valuable_quality
		utility += len(candidate.skills) * self.standard_quality

		# Calculate utility for GPA
		utility += candidate.gpa * self.gpa_scale_constant

		# Calculate utility for minors
		if candidate.minor_name != None:
			if candidate.minor_name == 'MATH' or candidate.minor_name == 'BUSINESS':
				utility += self.valuable_quality
			else:
				utility += self.standard_quality

		# Utility for experience/internships
		utility += candidate.years_experience * self.valuable_quality

		# Add extra utility for masters' students
		if candidate.degree_name == 'MASTERS_CS' or candidate.degree_name == 'MASTERS_CE':
			utility += self.valuable_quality

		# Return normalized utility between 1 and 10
		return round((utility/self.max_candidate_ut)*10, 2)


	def calculateEmployerBaseUtility(self, employer):
		# Determines basic quality of an employer based on candidate requirement criteria for software position
		utility = 0

		# Include GPA in utility calculation
		utility += employer.min_gpa * self.gpa_scale_constant

		# Required years of experience goes into the quality of the position
		utility += employer.required_years_experience

		# Add the factor of the length of preferred skills list
		utility += len(employer.preferred_skills)

		# Extra utility if they are looking for a masters student
		if employer.preferred_degree_name == 'MASTERS_CS' or employer.preferred_degree_name == 'MASTERS_CE':
			utility += self.valuable_quality

		return (utility/self.max_employer_ut)*10

	def calculateInitialMatchUtility(self, employer, candidate):
		utility = candidate.base_utility

		# Field of study utility
		if employer.preferred_degree_name == candidate.degree_name:
			utility += self.valuable_quality * employer.weights['preferred_degree_name']

		# Preferred work category utility
		if employer.preferred_candidate_category == candidate.experience_category:
			utility += self.valuable_quality * employer.weights['preferred_candidate_category']

		# Minimum GPA utility
		if candidate.gpa >= employer.min_gpa:
			utility += self.standard_quality * employer.weights['min_gpa']

		# Minor utility
		if candidate.minor_name == employer.preferred_minor_name:
			utility += self.standard_quality * employer.weights['preferred_minor_name']

		# Skills utility
		skills = 0
		for s in employer.preferred_skills:
			if s in candidate.proficient_languages or s in candidate.skills:
				skills += 1
		utility += skills * employer.weights['preferred_skills']

		# Years of experience utility
		if candidate.years_experience >= employer.required_years_experience:
			utility += employer.weights['required_years_experience'] * (candidate.years_experience - employer.required_years_experience)

		# Coding Exam: random gaussian distribution with higher standard deviation the lower the GPA
		gpa_score = (candidate.gpa/4.0)*8.0
		if 10.0 - gpa_score <= 2.5:
			stdev = 1.0
		elif 10.0 - gpa_score > 2.5 and 10.0 - gpa_score < 4.0:
			stdev = 2.0
		else:
			stdev = 3.0

		exam_score = random.gauss(gpa_score, stdev)
		if exam_score > 10.0:
			exam_score = 10.0
		elif exam_score < 0.0:
			exam_score = 0.0

		utility += exam_score * employer.weights['coding_exam']

		# Personality score utility
		utility += employer.weights['personality_score'] * candidate.personality_score

		# Project evaluation: review each project, give each a score, normalize them and add them to the total utility
		project_utilities = []
		for project in candidate.projects:
			u = 0
			if project.job_category == employer.preferred_candidate_category:
				u += self.valuable_quality * employer.weights['projects']
			for skill in project.skills:
				if skill in employer.preferred_skills:
					u += self.valuable_quality
			if project.project_type == 'personal':
				u += self.valuable_quality * employer.weights['projects']
			u *= project.length_in_months
			project_utilities.append(u)

		# normalized_project_utilities = [float(u)/max(project_utilities) for u in project_utilities]
		for ut in project_utilities:
			utility += ut

		return utility

	def calculateFinalMatchUtility(self, employer, candidate):
		utility = candidate.base_utility

		# Personality score utility
		utility += (employer.weights['personality_score'] * candidate.personality_score) * self.valuable_quality


		return utility

