""" This is a practice ground of concurrenc and async concepts """

# Imports #
from agents import Agent, Runner

from dotenv import load_dotenv
load_dotenv(override=True)

# Initiate an Agent #
instructions = "You are a polite and helpful assistant"
my_agent = Agent(name="personal assistant", model="gpt-5.4-mini", )

# Async Function Cases #

# 1. When your function has to call a library function that requires/supports ´await´,
#   then your function should be defines async def

async def query_agent(query: str):
    response = await Runner.run(my_agent, query)
    return (response.final_output)

# 2. When your function does not communicate with any external database, function, api etc. (for whatever reason)
#    then, you can define the function as 

async def add_function_1(a: int, b: int):
    return a+b

# Non Async functions  #

# 1. If your function calls another function, or a library function that does not support ´await´
#    then, you should define you function with a normal ´def´

def support_func(a: int, b:int) -> int:  # This is a regular function
    return a+b

def add_function_2(a: int, b: int) -> int:
    sum = support_func(a,b)              # this is invalid: sum = await support_func(a,b), because support_func() doesn't support await 
    return sum
