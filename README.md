# LangChain Agents

This repository contains two examples of LangChain agents demonstrating different approaches to building AI assistants with Claude 3 Sonnet via Amazon Bedrock.

## Projects

### 1. Built-In-Tools-Starter-Example

Uses LangChain's built-in tools to create an agent that can:
- Search Wikipedia
- Run web searches with DuckDuckGo
- Execute Python code for calculations

### 2. Custom-Tool-Example

Implements a custom Spotify recommendation tool that:
- Takes a list of artists and desired number of tracks
- Interfaces with Spotify API to fetch top songs
- Returns randomized music recommendations from the artists' catalogs

## Setup

Both projects require:
- AWS credentials for Bedrock access
- Python 3.9+
- Required packages installed via `pip install -r requirements.txt`

The Spotify example additionally requires Spotify API credentials set in the `.env` file.

## Usage

To run the built-in tools example:
```
python Built-In-Tools-Starter-Example/agent.py
```

To run the Spotify recommender:
```
python Custom-Tool-Example/agent.py
``` 