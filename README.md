# yotify-web-app
This project provides a Flask-based web application to convert Spotify playlists into YouTube Music playlists. It uses the Spotipy library to interact with Spotify and the YTMusicAPI to handle YouTube Music operations.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Configuration](#configuration)
- [License](#license)

## Features
- Convert Spotify playlists to YouTube Music playlists.
- Create a new public playlist on YouTube Music.
- Add all tracks from a Spotify playlist to the new YouTube Music playlist.
- View playlist details and status of track additions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. Create venv:
   ```bash
   python -m venv venv
   venv\Scripts\activate
3. Install required packets:
   ```bash
   pip install -r requirements.txt
4. Create a .env folder mimicking the .env.example provided and add your credentials
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

## Usage
1. Run the flask app
   ```bash
   python app.py
2. Open your web browser and navigate to http://localhost:5000 to access the application.
3. Follow the instructions and convert whichever Spotify playlist you wish.
4. The app will return you a youtube music playlist and whether each song was successfully added or not.

## File Descriptions

- **`app.py`**: The main Flask application file. Handles routing, playlist conversion, and interacts with Spotify and YouTube Music APIs.
- **`yt_auth_jsonfile.py`**: Creates and manages the `browser.json` file used for authenticating with YouTube Music.
- **`utils.py`**: Contains utility functions for managing playlists and converting links.
- **`credentials.py`**: Loads Spotify client credentials and YouTube Music request headers from environment variables.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`.env.example`**: Example environment variables file. Copy this file to `.env` and add your credentials.

## Configuration
- Ensure you have valid Spotify API credentials and configure them in the `.env` file. The YouTube Music authentication is managed automatically through `yt_auth_jsonfile.py`. 
- If you wish to directly add the playlist directly into your account then just edit the "reference_header" parameter into your own through going on google, open ytmusic, inspect element->network-> and copy the reference header of whichever POST request that has youtubemusic in it.

## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.
