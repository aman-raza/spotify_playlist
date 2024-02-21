from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "325977a18b6e4b67ba99a653913b6787"
CLIENT_SECRET = "73e1019381e84368b8232bfafaf140a4"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read",
                                               show_dialog=True,
                                               cache_path="token.txt"))
results = sp.current_user_saved_tracks()
current_user_id = sp.current_user()["id"]
my_playlist = sp.user_playlist_create(user=current_user_id, name="test_2017", public=True, collaborative=False, description="time_travel")


response = requests.get("https://www.billboard.com/charts/hot-100/2017-08-12/")
bill_board = response.text
soup = BeautifulSoup(bill_board, 'html.parser')

song_titles = []

for song in soup.select("li ul li h3"):
    song_titles.append(song.getText().strip())

sp.playlist_add_items(playlist_id=my_playlist["id"], items=song_titles)
