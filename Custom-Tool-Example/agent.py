from langchain.agents import initialize_agent
from langchain.agents import AgentType
import os
from dotenv import load_dotenv

# Import tools and bedrock client
from bedrock_client import get_claude_llm
from custom_tool import get_tools

def main():
    """Main function to initialize and run the Spotify recommendation agent."""
    
    # Load environment variables
    load_dotenv()
    
    # Bedrock Claude 3 Sonnet setup
    llm = get_claude_llm(temperature=0.7, max_tokens=1024)
    
    # Get Spotify tool
    tools = get_tools()
    
    # Agent initialization
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,  # Handle parsing errors gracefully
    )
    
    # Example query with properly formatted artists list - make sure to use a Python list format
    query = 'I like the following artists: ["Arijit Singh", "Future", "The Weeknd"], can I get 12 song recommendations with them in it.'
    
    try:
        response = agent.run(query)
        print(f"\nRecommended Songs: {response}")
    except Exception as e:
        print(f"Error running agent: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
