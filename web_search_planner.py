from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 5

INSTRUCTIONS = f"""You are a helpful research assistant.
Given a user query, generate exactly {HOW_MANY_SEARCHES} effective web search queries that together would provide the most comprehensive information to answer it.
For each search, provide a brief reason why it is important and the exact search query.
Output only the structured list without additional text."""

class WebSearchItem(BaseModel):
    reason: str = Field(description = "Your reasoning for why this search is important to the query.")
    query: str = Field(description = "The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description = "A list of web searches to perform to best answer the query.")
    
web_search_planner_agent = Agent(
    name = "WebSearchPlannerAgent",
    instructions = INSTRUCTIONS,
    model = "gpt-4o-mini",
    output_type = WebSearchPlan,
)