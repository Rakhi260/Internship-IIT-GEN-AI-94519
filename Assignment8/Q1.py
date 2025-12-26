from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents.middleware import wrap_model_call
import os
import json
import requests

#ENV
load_dotenv()


# @wrap_model_call
# def model_logging(request, handler): #logging middleware
#     print("Before call:",'-'*20)
#     print(request)
#     response = handler(request) #sends request to model
#     print("After call:",'-'*20)
#     print(response)
#     response.result[0].content = response.result[0].content.upper()
#     return response

# @wrap_model_call
# def limit_model_context(request, handler): #context limiter
#     print("*Before model call: ",'-'*20)
#     #print(request)
#     request = request.override(messages=request.messages[-5:]) #keeps only last 5 messages
#     response = handler(request) #sends request to model
#     print("*After model call:",'-'*20)
#     print(response)
#     response.result[0].content = response.result[0].content.upper() #modifies output
#     return response

#TOOLS
@tool
def calculator(expression: str) -> str:
    """
    This is calculator function solves any arithmetic expression containing all constant value.
    It supports basic arithmetic operators +,-,*,/, and paranthesis.
    

    :param exp: str input arithmetic expression
    : returns expression result as str 
    """
    try:
        return str(eval(expression))
    except Exception:
        return "Error: Invalid arithmetic expression"


@tool
def get_weather(city):
    """
    This weather_tool gives current weather of a city,
    If weather of given city cannot found, return the "Error".
    This function doesn't return historic or general weather of the city
    If you get any prompt related to get weather call the tool get_weather.
    
    :param city: str input - city name
    : return current weather in json format or error
    """
    try:
        api_key = os.getenv("OPEN_WEATHER_API")
        url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&units=metric&q={city}"
        response = requests.get(url)
        weather = response.json()
        return json.dumps(weather)
    except:
        return "error"


@tool
def read_file(filepath: str) -> str:
    """
    ONLY use this tool when the user explicitly provides a FULL FILE PATH
    like C:/Users/.../file.txt or /home/user/file.txt.
    DO NOT use this tool for weather, math, definitions, or general questions.
    """
    try:
        with open(filepath, "r") as file:
         return file.read()
    except FileNotFoundError:
        return "Error:File not found"
    except Exception as e:
        return f"error finding file {e}"
        
    
@tool
def knowledge_lookup(query: str) -> str:
    """
    Looks predefined knowledge based on query
    """
    knowledge_base = {
        "python": "Python is a high-level programming language.",
        "langchain": "LangChain helps build LLM-powered applications.",
        "lm studio": "LM Studio runs LLMs locally on your machine."
    }

    return knowledge_base.get(query.lower(), "No knowledge found.")

#MODEL
llm = init_chat_model( # This connects LangChain to: LM Studio Running locally on your machine
    model="qwen/qwen3-4b-2507",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy-key"
)

#AGENT
agent = create_agent(#creates intelligent agent
    model=llm,
    tools=[calculator, get_weather, read_file,knowledge_lookup], #agent decides when to use which tool
  #  middleware = [model_logging, limit_model_context],
    system_prompt="""You are a helpful assistant. Answer briefly and clearly.
                   Tool usage rules:
                   -use calculator for math expression
                   -use get_weather to answer weather questions
                   -Use read_file only when user provides full file path
                   -Do not guess file paths
                   -use knowledge_lookup for definiton style questions 
                   -if prompt is not related to tool give answers based on your knowledge
                   answer all questions briefly and clearly
                   -If you get any prompt related to get weather call the tool get_weather
                   """ #controls agent behaviour
)

#CHAT
conversation = [] #stores chat history
while True: #continuous chat
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    conversation.append({"role":"user","content":user_input}) #adds user message

    response = agent.invoke({
        "messages": conversation     #Agent:
                                     #Reads messages
                                     #Chooses tools if needed
                                     #Calls LLM
                                     #Middleware runs
                                     #Returns result
    })
    
    ai_msg = response["messages"][-1]
    print("AI msg:", ai_msg.content)
    conversation = response["messages"]
