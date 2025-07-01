from dotenv import load_dotenv
load_dotenv()
from agents import Agent, Runner
import time

agent = Agent(name="Assistant", instructions="You are a helpful assistant",)



result = Runner.run_sync(agent, "Write a haiku about for  loop  in programming.")

for i in range(0, 5):
 
    print("<robo>")    
    result = (result.final_output)
    print("AI ass", result)
    time.sleep(5)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.