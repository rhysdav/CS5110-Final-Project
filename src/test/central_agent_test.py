from agent.CentralAgent import CentralAgent

def run_test_1():
    central_agent = CentralAgent()
    central_agent.initialize()
    print('Central agent initialization successful')
    central_agent.arm_pull_1()
    print('Arm pull 1 successful')
    central_agent.arm_pull_2(4)
    print('Arm pull 2 (with k = 4) successful')
    central_agent.arm_pull_3()
    print('Arm pull 3 successful')

    central_agent.salary_negotiation()
    print('Salary negotiation successful')
