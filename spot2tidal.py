import subprocess
import re
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials

# Function to fetch Spotify track details
def fetch_spotify_track_details(track_id):
    client_credentials_manager = SpotifyClientCredentials(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    track_info = sp.track(track_id)
    song_title = track_info['name']
    artist_name = ', '.join(artist['name'] for artist in track_info['artists'])
    duration_ms = track_info['duration_ms']
    duration_seconds = duration_ms // 1000
    return song_title, artist_name, duration_seconds

# Function to obtain the standard web URL from a mobile app short URL using requests
def convert_mobile_url_to_web_url(mobile_url):
    try:
        # Send a GET request to the mobile URL and follow redirects
        response = requests.get(mobile_url, allow_redirects=True)
        
        # Extract the final URL after redirects
        web_url = response.url

        # Extract the track ID from the mobile URL
        match = re.search(r'/track/([\w\d]+)', web_url)
        if match:
            track_id = match.group(1)
        else:
            raise Exception("Failed to extract track ID from the URL")

        return track_id

    except Exception as e:
        raise Exception(f"Failed to obtain web URL from mobile URL: {e}")

# Get the Spotify track link from the user
spotify_link = input("Enter the Spotify Track Link: ")

try:
    # Check if the link is a mobile app short URL or a standard web URL
    match = re.match(r'^(https://(?:open\.spotify\.com/track/|spotify\.com/track/|spotify\.link/)([\w\d]+)(?:\?.*)?)$', spotify_link)
    if match:
        # Extract the track URL and track ID from the match
        track_url = match.group(1)
        track_id = match.group(2)

        # If it's a mobile app short URL, convert it to a standard web URL
        if "spotify.link" in track_url:
            track_id = convert_mobile_url_to_web_url(track_url)

        # Fetch Spotify track details using the track ID
        song_title, artist_name, duration_seconds = fetch_spotify_track_details(track_id)

        # Generate a search command for orpheus.py and display it
        query = f'{song_title} {artist_name}'
        orpheus_search_command = f'python3 ../orpheus.py search tidal track "{query}"'

        print(f"Executing the following command to search on Tidal:\n\n{orpheus_search_command}\n")
        print("This command will search for the track on Tidal.")
        print("You can copy and paste this command into your terminal to continue with the search on Tidal.")

        # Execute the orpheus.py search command
        subprocess.run(orpheus_search_command, shell=True)

    else:
        raise ValueError("Invalid Spotify link format")

except Exception as e:
    print(f"Error: {e}")
