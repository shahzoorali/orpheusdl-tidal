# spot2tidal.py

`spot2tidal.py` is a Python script that integrates Spotify and Tidal, allowing you to search for Spotify tracks on Tidal using the `orpheus.py` script from the `orpheusdl-tidal` repository.

## Prerequisites

- Have Spotify account for API KEYS (https://developer.spotify.com/dashboard)
- Already have OrpheusDL installed and configured (https://github.com/OrfiTeam/OrpheusDL)
- Python 3.x
- Required Python libraries:
  - `spotipy`
  - `requests`
- `orpheusdl-tidal` repository

## Setup / Dependancy

MAKE SURE TO CHANGE WITH YOUR 'client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET'' in spot2tidal.py file (line #9)
Grab from https://developer.spotify.com/dashboard

1. **Clone the `orpheusdl-tidal` Repository:**

   Clone the repository to your local machine by running:
   ```sh
   git clone https://github.com/Dniel97/orpheusdl-tidal.git
   cd orpheusdl-tidal

## USAGE

run spot2tidal.py (python spot2tidal.py)
It prompts for spotify URL. Enter the URL, it will search on Tidal and prompts you to choose from search results. This will download the track from Tidal.