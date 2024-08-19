import pickle
import streamlit as st
import requests
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace with your Spotify client ID and secret
client_id = r'1befb8d597e442efbaa2dd1c8303fa08'
client_secret = r'a0801d9649374ac3b33567acbe257c21'

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_album_cover(album_uri):
  
  album = sp.album(album_uri)
  album_cover_url = album['images'][0]['url']
  return album_cover_url

def recommend(song):
    index = songs[songs['track_name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_song_names = []
    recommended_song_posters = []
    for i in distances[1:len(distances)]:
        # fetch the movie poster
        
        if songs.iloc[i[0]].track_name not in recommended_song_names and len(recommended_song_names)<=10 and songs.iloc[i[0]].track_name!=song:
            recommended_song_names.append(songs.iloc[i[0]].track_name)
        if len(recommended_song_names)==10:
            break
    for song in recommended_song_names:
        song_id = songs[songs['track_name']==song]['uri'].iloc[0]
        recommended_song_posters.append(get_album_cover(song_id))

    return recommended_song_names,recommended_song_posters


st.header('Music Recommender System')
songs = pickle.load(open('track_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

songs_list = songs['track_name'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    songs_list
)



if st.button('Show Recommendation'):
  recommended_song_names, recommended_song_posters = recommend(selected_song)
  cols = st.columns(10)

  for i, col in enumerate(cols):
    with col:
      st.text(recommended_song_names[i])
      st.image(recommended_song_posters[i])