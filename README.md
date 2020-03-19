# CS 5110 Final Project: New Graduate Selection
_Rhys Davies, Alec Jackson, Jason Boyd_

**Abstract**

How should employers in the software field narrow a list of new graduate candidates from a computer science department at 
a university to include only the best-suited candidates that meet their criteria? We propose implementing a centralized 
agent that uses combinatorial pure exploration (CPE) to perform costly exploration of a set of arms of new 
graduate candidates. Employers will specify minimum criteria to the centralized agent, which will in turn explore the set 
of arms with a given number of candidates. We will examine what number of candidates must be given to 
each individual agent (or arm) to produce a candidate which meets the criteria set by the employer. 
We will also examine what portion of agents find a candidate from the computer science department at Utah State University 
given that threshold, and conclude what portion of Utah State University computer science students are qualified for real-world software positions.

## Meeting Notes

**Rough Program Steps**

1. The first pull will acquire the top-k utilities from the candidates.
    - each piece of the candidate will be assigned a utility that coincides with their desired field of work.
    - an overall utility will be calculated from those utility pieces that will be used for candidate selection.
2. Each subsequent pull will randomly add or subtract a certain amount of utility (simulating employers learning about candidates).
    - the second pull could possibly look at the employer's utility pieces and pull candidates who score higher with that employer.
3. The last pull will be random as well (how well the candidate blends with the team).

**Step 1: Generating Data**

* Candidate Generation
* Employer Generation
* Utility Generation
