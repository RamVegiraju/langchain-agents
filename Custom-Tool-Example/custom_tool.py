from pydantic import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os
import re
import ast
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Spotify credentials from environment variables
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Instantiate spotipy client
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
))

class MusicInput(BaseModel):
    artists: list[str] = Field(description="A list of artists that they'd like to see music from")
    tracks: int = Field(description="The number of tracks/songs they want returned.")

class SpotifyTool(BaseTool):
    name: str = "Spotify Music Recommender"
    description: str = "Use this tool when asked music recommendations."
    args_schema: Type[BaseModel] = MusicInput
    
    # utils
    @staticmethod
    def retrieve_id(artist_name: str) -> str:
        results = sp.search(q='artist:' + artist_name, type='artist')
        if len(results) > 0:
            artist_id = results['artists']['items'][0]['id']
        else:
            raise ValueError(f"No artists found with this name: {artist_name}")
        return artist_id

    @staticmethod
    def retrieve_tracks(artist_id: str, num_tracks: int) -> list:
        if num_tracks > 10:
            raise ValueError("Can only provide up to 10 tracks per artist")
        tracks = []
        top_tracks = sp.artist_top_tracks(artist_id)
        for track in top_tracks['tracks'][:num_tracks]:
            tracks.append(track['name'])
        return tracks

    @staticmethod
    def all_top_tracks(artist_array: list) -> list:
        complete_track_arr = []
        for artist in artist_array:
            artist_id = SpotifyTool.retrieve_id(artist)
            all_tracks = {artist: SpotifyTool.retrieve_tracks(artist_id, 10)}
            complete_track_arr.append(all_tracks)
        return complete_track_arr

    # main execution
    def _run(self, artists: list, tracks: int) -> list:
        num_artists = len(artists)
        max_tracks = num_artists * 10
        print("---------------")
        print(artists)
        print(type(artists))
        print("---------------")
        all_tracks_map = SpotifyTool.all_top_tracks(artists) # map for artists with top 10 tracks
        all_tracks = [track for artist_map in all_tracks_map for artist, tracks in artist_map.items() for track in tracks] #complete list of tracks

        if tracks > max_tracks:
            raise ValueError(f"Only 10 tracks per artist, max tracks for this many artists is: {max_tracks}")
        final_tracks = random.sample(all_tracks, tracks)
        return final_tracks

    def _arun(self):
        raise NotImplementedError("Spotify Music Recommender does not support ")

def get_tools():
    """Initialize and return the Spotify tool."""
    tools = [SpotifyTool()]
    return tools 