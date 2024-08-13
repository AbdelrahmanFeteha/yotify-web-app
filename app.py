import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
import ytmusicapi
from ytmusicapi.exceptions import YTMusicError, YTMusicServerError

from credentials import ClientID, ClientSecret
from utils import add_song_in_yt_playlist, display_playlist_terminal, link_to_id, display_account_info, yt_id_to_link
import yt_auth_jsonfile      #this will create the browser.json file

#create a spotify object
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=ClientID, client_secret=ClientSecret))

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  #this is my secret key for this flask app

#url endpoint for the home page
@app.route('/')
def index():
    return render_template('index.html')

#url endpoint for the convert page
@app.route('/convert', methods=['POST'])
def convert():
    sp_playlist_link = request.form['sp_playlist_link']
    yt_playlist_name = request.form['yt_playlist_name']
    description = request.form['description']
    
    sp_playlist_id = link_to_id(sp_playlist_link)
    if sp_playlist_id is None:
        flash("Invalid Spotify Playlist Link", 'error')
        return redirect(url_for('index'))
    
    #create a ytmusic object
    ytmusic = ytmusicapi.YTMusic("browser.json")
    
    account_info = ytmusic.get_account_info()
    display_account_info(account_info)  #display account info in the terminal
    
    try:
        my_sp_playlist = sp.playlist(sp_playlist_id)
        display_playlist_terminal(my_sp_playlist)
    except SpotifyException as e:
        flash(f"Error in getting playlist data\nError code: {e.http_status} Error message: {e.msg}", 'error')
        return redirect(url_for('index'))
    try:
        #create a PUBLIC playlist
        yt_playlist_id = ytmusic.create_playlist(yt_playlist_name, description, privacy_status='PUBLIC')
        #this will store the status and name of each song that is added to the playlist
        #the songs will be added to the playlist
        track_status = []
        for track in my_sp_playlist['tracks']['items']:
            try:
                song_title = track['track']['name']
                status = add_song_in_yt_playlist(track, ytmusic, yt_playlist_id) 
                track_status.append({"status": status, "title": song_title})
            except Exception as e:
                track_status.append(f"Error adding track {track['track']['name']}: {e}")
                
        playlist_link = yt_id_to_link(yt_playlist_id)
        print("terminal result: ", playlist_link)
        flash(f"Your playlist {yt_playlist_name} has been created successfully and songs have been added to {account_info['accountName']}'s account!", 'success')
        return render_template('result.html',
                                yt_playlist_name=yt_playlist_name,
                                track_status=track_status,
                                sp_playlist_name = my_sp_playlist['name'],
                                sp_playlist_desc= my_sp_playlist['description'],
                                sp_playlist_owner = my_sp_playlist['owner']['display_name'],
                                sp_playlist_mins = my_sp_playlist['tracks']['total'],
                                sp_playlist_num_tracks = len(my_sp_playlist['tracks']['items']),
                                playlist_link = playlist_link)
    except YTMusicServerError as e:
        if 'too many playlists' in str(e):
            flash('You are creating too many playlists. Please wait a while before creating further playlists.', 'error')
        else:
            flash('An error occurred: ' + str(e), 'error')
    except YTMusicError as e:
        flash('An error occurred: ' + str(e), 'error')
    return redirect(url_for('index'))

if __name__ == "__main__":
    #host = '0.0.0.0' broadcast address --> to all devices on the network
    app.run(port = 5000, debug = True  )

