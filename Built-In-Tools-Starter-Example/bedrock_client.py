import boto3
import os
from dotenv import load_dotenv
from langchain_community.chat_models import BedrockChat

# Load environment variables
load_dotenv()

def get_bedrock_client():
    """Initialize and return an Amazon Bedrock client."""
    
    # AWS credentials should be in .env file
    aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION", "us-east-1")  # Default to us-east-1 if not specified
    
    # Create a Bedrock client
    bedrock_client = boto3.client(
        service_name="bedrock-runtime",
        region_name=aws_region,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    
    return bedrock_client

def get_claude_llm(temperature=0, max_tokens=1024):
    """Initialize and return a Claude 3 Sonnet LLM via Bedrock."""
    
    bedrock_client = get_bedrock_client()
    
    # Initialize Claude 3 Sonnet model using BedrockChat
    llm = BedrockChat(
        client=bedrock_client,
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",  # Claude 3 Sonnet model ID
        model_kwargs={
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": 0.9,
        }
    )
    
    return llm 