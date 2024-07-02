# spot2tidal.py

`spot2tidal.py` is a Python script that integrates Spotify and Tidal, allowing you to search for Spotify tracks on Tidal using the `orpheus.py` script from the `orpheusdl-tidal` repository.

## Prerequisites

- Already have OrpheusDL installed and configured (https://github.com/OrfiTeam/OrpheusDL)
- Python 3.x
- Required Python libraries:
  - `spotipy`
  - `requests`
- `orpheusdl-tidal` repository

## Setup / Dependancy

1. **Clone the `orpheusdl-tidal` Repository:**

   Clone the repository to your local machine by running:
   ```sh
   git clone https://github.com/Dniel97/orpheusdl-tidal.git
   cd orpheusdl-tidal

## USAGE

run spot2tidal.py (python spot2tidal.py)
It prompts for spotify URL. Enter the URL, it will search on Tidal and prompts you to choose from search results. This will download the track from Tidal.