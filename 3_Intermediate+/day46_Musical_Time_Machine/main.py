#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT_ID = "" # YOUR SPOTIFY CLIENT ID HERE
SPOTIFY_CLIENT_SECRET = "" # YOUR SPOTIFY CLIENT SECRET HERE

# Scraping Billboard 100
user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{user_date}"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
artists = soup.find_all(name="span", class_="chart-element__information__artist text--truncate color--secondary")
song_titles = [song.getText() for song in songs]
artist_names = [artist.getText() for artist in artists]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = user_date.split("-")[0]
for song, artist in zip(song_titles, artist_names):
    result = sp.search(q=f"track: {song} artist: {artist}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
