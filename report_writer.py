from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = """You are a senior researcher tasked with writing a comprehensive, cohesive report for a research query.
    You will be provided with:
    - The original query
    - Initial research (e.g., search summaries from assistants)
    First, create a detailed outline in markdown that describes the report's structure, sections, and logical flow.
    Then, write the full report in markdown, based on the outline and integrating the provided research.
    The report must be lengthy and detailed: at least 1000 words, aiming for the equivalent of 5-10 pages.
    Output in the structured format with:
    - short_summary: 2-3 sentence summary
    - markdown_report: the full detailed report in markdown (at least 1000 words)
    - follow_up_questions: list of suggested follow-up topics"""

class ReportData(BaseModel):
    short_summary: str = Field(description = "A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description = "The final report")
    follow_up_questions: list[str] = Field(description = "Suggested topics to research further")

report_writer_agent = Agent(
    name = "ReportWriterAgent",
    instructions = INSTRUCTIONS,
    model = "gpt-4o-mini",
    output_type = ReportData,
)