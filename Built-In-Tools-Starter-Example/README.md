# LangChain Agent with Claude 3 Sonnet via Bedrock

This project implements a LangChain agent powered by Claude 3 Sonnet through Amazon Bedrock. The agent can use various tools including Wikipedia search, web search, and a Python REPL.

## Project Structure

- `agent.py` - Main script that initializes and runs the agent
- `bedrock_client.py` - Handles the Bedrock client and Claude 3 LLM setup
- `tools.py` - Defines the tools available to the agent
- `.env` - Contains AWS credentials (not tracked in git)
- `requirements.txt` - Project dependencies

## Setup

1. Ensure you have Python 3.8+ installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure your `.env` file with AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=your_access_key
   AWS_SECRET_ACCESS_KEY=your_secret_key
   AWS_REGION=your_region  # Optional, defaults to us-east-1
   ```

## Usage

Run the agent with:

```
python agent.py
```

To modify the agent's behavior:

1. Edit the query in `agent.py` to ask different questions
2. Adjust model parameters in `bedrock_client.py`
3. Add or modify tools in `tools.py`

## Extending the Agent

To add additional tools:
1. Import the desired tools in `tools.py`
2. Add them to the tools list in the `get_tools()` function 