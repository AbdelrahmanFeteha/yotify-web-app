def display_account_info(account_info):
    print ("Moving songs to the following account:")
    print (f"Account Name: {account_info['accountName']}")
    print (f"Account Photo URL: {account_info['accountPhotoUrl']}")


def link_to_id(link):
    parts = link.split("/")
    playlist_with_query = parts[-1]
    playlist_id = playlist_with_query.split("?")[0]
    if len(playlist_id) == 22:
        return playlist_id
    else:
        print ("Invalid Spotify Playlist Link") # for terminal
        return None

def yt_id_to_link(playlist_id):
    return f"https://music.youtube.com/playlist?list={playlist_id}"
    
    
def add_song_in_yt_playlist (track, ytmusic, yt_playlist_id):
    try:
        search_results = ytmusic.search(track['track']['name']) #this returns a list of dictionaries
        if search_results:
            video_id = search_results[0]['videoId']
            ytmusic.add_playlist_items(yt_playlist_id, [video_id])
            print (f"The song {track['track']['name']} has been added succesfully to your new playlist!")
            return "Success"
        else:
            print (f"Could not find the song {track['track']['name']} on Youtube Music")
            return "Not found"
    except Exception as e:
        print(f"An error occurred while adding the song {track['track']['name']}: {e}")
        return "Error adding song"
            
def display_playlist_terminal(playlist):    
    print ("Playlist Name: ", playlist['name'])
    print ("Description: ", playlist['description'])
    print ("Number of tracks: ", len(playlist['tracks']['items']))
    print (f"Owner: {playlist['owner']['display_name']}")
    print (f"Total duration: {playlist['tracks']['total']} minutes")