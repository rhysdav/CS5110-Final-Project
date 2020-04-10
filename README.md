# CS 5110 Final Project: New Graduate Selection
_Rhys Davies, Alec Jackson, Jason Boyd_

**Abstract**

How should employers in the software field narrow a list of new graduate candidates from a computer science department at a university to include only the best-suited candidates that meet their criteria? We propose implementing a centralized agent that uses combinatorial pure exploration (CPE) to perform costly exploration of a set of arms of new graduate candidates. Employers will specify minimum criteria to the centralized agent, which will in turn explore the set of arms with a given number of candidates. We will examine what number of candidates must be given to each individual agent (or arm) to produce a candidate which meets the criteria set by the employer.

We will also examine what portion of agents find a candidate from the computer science department at Utah State University given that threshold, and conclude what portion of Utah State University computer science students are qualified for real-world software positions.

## Meeting Notes

**Rough Program Steps**

1. The first pull will acquire the top-k utilities from the candidates.
    - each piece of the candidate will be assigned a utility that coincides with their desired field of work.
    - an overall utility will be calculated from those utility pieces that will be used for candidate selection.
2. Each subsequent pull will randomly add or subtract a certain amount of utility (simulating employers learning about candidates).
    - the second pull could possibly look at the employer's utility pieces and pull candidates who score higher with that employer.
3. The last pull will be random as well (how well the candidate blends with the team).

### Step 1: Generating Data
The scope and timeframe of this project made it impractical to pursue data gathering methods such as surveys. However, generating our own mock data based on already available job postings and university coursework was not out of reach. While we may not be able to make definitive claims from this generated data, we can still observe general hiring patterns for new graduates in the field of Computer Science.

Again, to fit the scope of the project, we have chosen to limit employment fields to the following four categories, which we feel represent the majority of current job postings for new graduates: Mobile/Web Development, Data Science and Machine Learning, Embedded Systems, and Game Development.

##### Candidate Generation
Each candidate object contains the following traits which model a typical resume for a new graduate:
- Degree
- Minors (if any)
- GPA
- Languages and skills
- Years of experience
- Field of experience (if any)
- Personal / school projects
- Relevant coursework

For the purposes of the algorithm, each candidate also contains the following:
- Preferred job field which determines which jobs the candidate will apply for
- A minimum salary requirement, used in the final stages of the negotiation algorithm
- A personality score, to help simulate an interview interaction (arm pull #2)
- A base utility score, used to determine the first arm pull (please note that utility calculation is done after the initial candidate generation and is described in a later section)

A goal of this project was to explore whether new Computer Science graduates of USU are sufficiently qualified for real-world software positions.

To ensure that our generated candidates reflect the resumes of real USU graduates, we compiled our own course catalog replicated from the listed courses on USU's website. Each is additionally associated with a set of languages and skills used in that course.  Included in our course catalog are elective courses only. The languages and skills from required classes are automatically added to the candidate upon generation.  Elective courses are then added to the candidate based on USU's CS Bachelor Degree credit requirements. Our course catalog includes courses which would have been available to students graduating in the Spring 2020 semester.

The remaining candidate traits are generated somewhat randomly. The methods for each are described below.

- **Minor:** For the sake of simplicity, a candidate may have up to one minor. We have also limited the minors to Math, Business, or Other. We feel this accurately represents the majority of USU CS students as well as employer needs.
- **GPA:** A randomly generated float per candidate between 2.0 and 4.0, rounded to 2 decimal places.
- **Experience:** Years of experience are randomly generated per candidate from 0 to 4. If this value is greater than zero, an experience category is chosen from the four previously listed employment fields. A subset of languages and skills representative of that job's technology stack are then chosen and added to the candidate based on experience category.
- **Projects:** To facilitate project generation, we make use of a separate Candidate Project object which contains the following traits:
    - Category - from the aforementioned experience categories
    - Length in months
    - Languages and skills
    - Project type - school or personal

  Projects are generated in a fashion similar to experience, and take into account projects which would be completed in the candidate's courses. A candidate may have anywhere from 0 to 3 projects. While a real graduate may certainly have completed more than 3 projects during their academic career, it is unlikely that more than 3 could be included on a one-page resume.
- **Minimum salary:** A randomly generated integer per candidate between $35,000 and $50,000 in increments of $3,000.
- **Personality score:** A randomly generated integer between 1 and 10.
- **Preferred job category:** The option exists to generate candidates with a specific job preference category. When this is done, we generate candidates with the following percentages: 60% Mobile and Web Development, 20% Data Science and Machine Learning, 10% Embedded Systems, and 10% Game Development. If no job category is provided for a candidate, one is randomly generated, with weight given to the candidate's experience category, according to the number of years spent in that category.

A candidate's base utility is initially set to zero, and then updated prior to the first arm pull, as described below in Step #2.

While inaccuracies will exist between our generated candidates and real data, we feel we have done our best to represent USU students based on the university's available course listings as well as our own research into the existing job market.

##### Employer Generation

### Step 2: Utility Calculation and Arm Pulls
