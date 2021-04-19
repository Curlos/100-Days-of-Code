from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def find_top_100_songs():
    '''
    Scrapes and finds out what Billboard's The Hot 100 of a certain week was
    and returns the song name, artist and the user's date formatted as Month, Day, Year.
    '''
    entered_date = input("Enter a date in the format (YYYY-MM-DD): ")

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{entered_date}")
    billboard_100_html = response.text

    soup = BeautifulSoup(billboard_100_html, "html.parser")
    song_title_elements = soup.find_all(name="span",
                                        class_="chart-element__information__song text--truncate color--primary")
    song_artist_elements = soup.find_all(name="span",
                                        class_="chart-element__information__artist text--truncate color--secondary")
    entered_date_formatted = soup.find(name="button", class_="date-selector__button button--link").getText().replace('\n', '').strip()

    song_titles_and_artist = []

    for i in range(len(song_title_elements)):
        song_title = song_title_elements[i].getText()
        artist_first_name = song_artist_elements[i].getText().split(' ')[0] # Artist's first name only
        song_titles_and_artist.append(f"{song_title} {artist_first_name}")

    return (song_titles_and_artist, entered_date_formatted)


def create_and_add_to_playlist():
    '''
    Creates a spotify playlist that will then have more or less 100 songs added to it.
    Spotify does not have every piece of music on the planet in it's database
    so some songs will be missing and it will favor more recent years.
    '''
    top_100_songs = find_top_100_songs()
    top_100_songs_titles = top_100_songs[0]
    top_100_songs_date = top_100_songs[1]

    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    song_uris = []

    for song_title in top_100_songs_titles:
        result = sp.search(q=song_title, limit=1, offset=0, type='track', market=None)

        # If at least one search result was found, then that first search result
        # (which is usually the song we're looking for) will be added to the playlist
        if result['tracks']['items']:
            song_uri = result['tracks']['items'][0]['uri']
            song_uris.append(song_uri)
            print(f"Adding {song_title}...")

    user = os.getenv('SPOTIFY_USER_ID')
    top_100_playlist = sp.user_playlist_create(user=user, name=f"The Hot 100 Week of {top_100_songs_date}", public=True,
                                               collaborative=False, description="")
    playlist_id = top_100_playlist['uri']

    sp.playlist_add_items(playlist_id, song_uris, position=None)
    print('Spotify playlist created and songs added')

create_and_add_to_playlist()