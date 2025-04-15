from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
import os
from dotenv import load_dotenv

# import tools and bedrock client
from bedrock_client import get_claude_llm
from tools import get_tools

def main():
    """Main function to initialize and run the agent."""
    
    # Load environment variables
    load_dotenv()
    
    # Bedrock Claude Sonnet setup
    llm = get_claude_llm(temperature=0, max_tokens=2048)
    
    # Tools retrieved from tools.py
    tools = get_tools()
    
    # Agent initialization
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,  # Handle parsing errors gracefully
    )
    
    # Sample query 1
    query = "Calculate 4 + 4"
    # Sample query 2
    # query "What is the population of Japan divided by the number of islands it has?"
    try:
        response = agent.run(query)
        print(f"\nResponse: {response}")
    except Exception as e:
        print(f"Error running agent: {e}")

if __name__ == "__main__":
    main()