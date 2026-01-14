from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTIONS = """You are a research assistant.
    Given a search term, perform a web search for it.
    Then output only a concise summary of the results:
    - 2-3 paragraphs
    - Under 300 words
    - Capture main points and essence only
    - Write succinctly (fragments okay; no need for complete sentences or perfect grammar)
    - Ignore fluff and irrelevant details
    Do not add any introductions, commentary, or extra text."""

search_agent = Agent(
    name = "SearchAgent",
    instructions = INSTRUCTIONS,
    tools = [WebSearchTool(search_context_size = "low")],
    model = "gpt-4o-mini",
    model_settings = ModelSettings(tool_choice = "required"),
)