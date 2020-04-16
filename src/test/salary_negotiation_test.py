from agent.CentralAgent import CentralAgent
from random import choice

def check_runs():
    ca = CentralAgent()
    ca.initialize()
    print('Succesful CentralAgent initialization.')

    for employer in ca.employers:
        candidate = choice(ca.candidates)
        employer.qualified_candidates.append(candidate)
        if candidate not in ca.final_candidates:
            ca.final_candidates.append(candidate)

    ca.salary_negotiation()
    print('Salary negotiation didnt crash and burn, congrats.')
