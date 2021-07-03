from youtube_api import YouTubeDataAPI, parsers
import urllib.parse
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

api_key = input('Please enter YT api key: ')
yt = YouTubeDataAPI(api_key)

def get_list_id(pl_url):
    parsed_url = urllib.parse.parse_qs(pl_url)
    pl_id = str(parsed_url['list']).strip("[").strip("]").strip("'")
    return pl_id

pl_id = get_list_id(input('Insert playlist url here: '))

itemai = yt.get_videos_from_playlist_id(
    pl_id, 
    part=['snippet'],
    parser = parsers.raw_json
    )

titles = [item['snippet']['title'] for item in itemai]
print(titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth( client_id=input('Please input client ID: '),
                                                client_secret=input('Please input client secret: '),
                                                redirect_uri="http://localhost:9000",
                                                scope=scope))

user_id = sp.user(input('What is your user id? '))
pl_name = input('How would you like to name your playlist? ')

playlist = sp.user_playlist_create(user_id['id'], pl_name, public=False, collaborative=False, description=pl_name)

def find_song(title):
    search_results = sp.search(title, limit=1, type='track')
    return search_results['tracks']['items'][0]['id']

findings = []

for title in titles:
    try:
        findings.append(find_song(title))
    except:
        continue

append_track = sp.user_playlist_add_tracks(user_id['id'], playlist['id'], findings, position=None)
