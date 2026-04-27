import streamlit as st
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()
class AgentState(TypedDict):
    query: str
    decision: str
    tool_output: str
    final_answer: str

llm = ChatOpenAI(model="gpt-4o")
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_tool(state):
    try:
        response = tavily.search(state["query"], max_results=3)
        content = ""
        for r in result["results"]:
            content += f"Title: {r['title']}\nSnippet: {r['snippet']}\nURL: {r['url']}\n\n"

        if "weather" in state["query"].lower():
            prompt = "The query is about weather, so we should also check the current weather conditions."
        else:
            prompt = "The query is not about weather, so we can skip checking the weather conditions."

        formatted = llm.invoke(f"""You are an assistant that helps answer user queries. Here are the search results for the query "{state['query']}":
{content}
{prompt}""")

        return {"tool_output": formatted}
    except Exception as e:
        return {"tool_output": f"Error: {str(e)}"}

