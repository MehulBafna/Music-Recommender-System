# Music Recommender System

## A Spotify dataset of over 70,000 songs was processed to extract relevant metadata (artist, track, album, genre). This data was then transformed into numerical representations using count vectorization to create feature vectors for each song.
## Cosine similarity was computed between song vectors to identify similar tracks. The system generates top 10 song recommendations based on similarity scores.
## Album covers were fetched using the Spotify API and integrated into the recommendations. A user-friendly interface was developed using Streamlit to display recommended songs with their corresponding album art.
## The system employs a content-based filtering approach, recommending songs similar to the user’s previously listened tracks or preferred genres, without requiring explicit user ratings or behavior data.
