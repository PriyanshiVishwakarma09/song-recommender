import streamlit as st
import pandas as pd
import joblib

# Load data
df = pd.read_csv("songs.csv")
mood_map = joblib.load("mood_map.pkl")

st.title("🎵 Mood-Based Song Recommender")

mood = st.selectbox("Choose your mood", ["happy", "sad", "energetic", "calm"])

def recommend(mood, n=8):
    cluster = None

    for k, v in mood_map.items():
        if v == mood:
            cluster = k
            break

    songs = df[df['cluster'] == cluster]

    if mood == "happy":
        songs = songs.sort_values(by='valence', ascending=False)
    elif mood == "energetic":
        songs = songs.sort_values(by='energy', ascending=False)
    elif mood == "calm":
        songs = songs.sort_values(by='energy', ascending=True)
    elif mood == "sad":
        songs = songs.sort_values(by='valence', ascending=True)

    return songs.head(n)[['track_album_name', 'energy', 'valence']]

if st.button("Recommend"):
    result = recommend(mood)
    st.dataframe(result)