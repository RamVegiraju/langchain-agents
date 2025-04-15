from langchain.agents import Tool
from langchain.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_experimental.tools import PythonREPLTool
from langchain.utilities import WikipediaAPIWrapper

def get_tools():
    """Initialize and return a list of tools for the agent."""
    
    # Set up individual tools
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    search = DuckDuckGoSearchRun()
    python_tool = PythonREPLTool()
    
    # Create tool list
    tools = [
        Tool(
            name="Wikipedia",
            func=wikipedia.run,
            description="Useful for searching general knowledge topics, historical information, and facts. Use this when you need verified information from an encyclopedia."
        ),
        Tool(
            name="DuckDuckGo Search",
            func=search.run,
            description="Useful for current events, recent information, or topics not covered in Wikipedia. Use this to search the web for information."
        ),
        Tool.from_function(
            func=python_tool._run,
            name="Python REPL",
            description="Execute Python code for calculations, data analysis, or programmatic tasks. Use this when you need to compute something or run code."
        )
    ]
    
    return tools 