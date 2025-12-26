from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
import pandas as pd
import requests
import os
import json


@tool
def cal_tool(exp):
    """
    This is calculator function solves any arithmetic expression containing all constant value.
    It supports basic arithmetic operators +,-,*,/, and paranthesis.
    

    :param exp: str input arithmetic expression
    : returns expression result as str 

    """

    try:
        result = eval(exp)
        return str(result)
    except:
        print("Error!")

@tool
def weather_tool(city):
    """
    This weather_tool gives current weather of a city,
    If weather of given city cannot found, return the "Error".
    This function doesn't return historic or general weather of the city.
    
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
def read_file(filepath):
    """Read and return the content of a text file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except :
        return f"Error reading file:"
    
@tool
def knowledge_lookup(query: str) -> str:
    """Answer general knowledge questions using built-in knowledge."""
    # Simple stub – LLM will answer without external API
    return f"Knowledge lookup query received: {query}"


llm = init_chat_model(
    model="google/gemma-3-4b",
    model_provider="openai",
    base_url="http://127.0.0.1:1234/v1",
    api_key="dummy-key"

)

conversation = []

agent = create_agent(
    model=llm,
    tools=[cal_tool, 
           weather_tool,
           read_file],
    system_prompt = (
    "You are a helpful assistant,  use appropriate tool and answer in short."
    "Give 2-3 line summary about the output in simple english.")

)

while True:
    user_prompt = input("Ask: ")
    if user_prompt == "Exit":
        break
    conversation.append({"role": "user", "content": user_prompt})
    result = agent.invoke({
        "messages": conversation
    })
    
    ai_msg = result["messages"][-1]
    print("Ai msg:", ai_msg.content)
    conversation = result["messages"]