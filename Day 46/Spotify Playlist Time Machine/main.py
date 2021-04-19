from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def find_top_100_songs():
    entered_date = input("Enter a date in the format (YYYY-MM-DD): ") # "2000-08-12"

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{entered_date}")
    billboard_100_html = response.text

    soup = BeautifulSoup(billboard_100_html, "html.parser")
    song_title_elements = soup.find_all(name="span",
                                        class_="chart-element__information__song text--truncate color--primary")
    entered_date_formatted = soup.find(name="button", class_="date-selector__button button--link").getText().replace('\n', '').strip()

    song_titles = []

    for song_title_element in song_title_elements:
        song_titles.append(song_title_element.getText())

    return (song_titles, entered_date_formatted)


def create_and_add_to_playlist():
    top_100_songs = find_top_100_songs()
    top_100_songs_titles = top_100_songs[0]
    top_100_songs_date = top_100_songs[1]

    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    song_uris = []

    for song_title in top_100_songs_titles:
        result = sp.search(q=song_title, limit=1, offset=0, type='track', market=None)
        song_uri = result['tracks']['items'][0]['uri']
        song_uris.append(song_uri)

    user = os.getenv('SPOTIFY_USER_ID')
    top_100_playlist = sp.user_playlist_create(user=user, name=f"The Hot 100 Week of {top_100_songs_date}", public=True,
                                               collaborative=False, description="")
    playlist_id = top_100_playlist['uri']

    sp.playlist_add_items(playlist_id, song_uris, position=None)
    print('Spotify playlist created and songs added')

create_and_add_to_playlist()

