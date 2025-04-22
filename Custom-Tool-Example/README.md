# Spotify Music Recommender with LangChain and Claude 3

This example demonstrates how to create a custom LangChain tool that interfaces with the Spotify API to provide music recommendations. The agent uses Claude 3 Sonnet via Amazon Bedrock as the reasoning engine.

## Setup

1. Create a Spotify Developer account and register an application to get your Client ID and Secret
   - Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create a new app and get your Client ID and Secret

2. Set up your environment variables in a `.env` file:
   ```
   AWS_ACCESS_KEY_ID=your_aws_access_key
   AWS_SECRET_ACCESS_KEY=your_aws_secret_key
   AWS_REGION=your_aws_region
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the agent with:
```
python agent.py
```

The agent will use a sample query, but you can modify the `query` variable in `agent.py` to ask for recommendations based on different artists and number of tracks.

## Files

- `agent.py`: Main script that initializes and runs the agent
- `bedrock_client.py`: Sets up the Claude 3 Sonnet model via Amazon Bedrock
- `custom_tool.py`: Contains the custom Spotify tool implementation
- `requirements.txt`: Required packages

## How It Works

1. The agent receives a query asking for music recommendations based on specific artists
2. It uses the custom Spotify tool to:
   - Find the Spotify IDs for the specified artists
   - Retrieve the top tracks for each artist
   - Randomly select the requested number of tracks from the pool
3. The result is a list of recommended songs from the specified artists

## Limitations

- Each artist is limited to a maximum of 10 tracks
- The total number of tracks requested cannot exceed the number of artists × 10
