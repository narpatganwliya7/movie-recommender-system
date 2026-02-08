import streamlit as st
import pickle
import requests
import os

# ---------- PATH SAFE ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- LOAD DATA ----------
movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))
top_similar = pickle.load(open(os.path.join(BASE_DIR, 'top_similar.pkl'), 'rb'))

movies_list = movies['title'].values

# ---------- TMDB POSTER ----------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=93e94eba147c580143bcf33ece414110&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()

        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return None
    except:
        return None

# ---------- RECOMMENDER ----------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    similar_indices = top_similar[movie_index]

    recommended_movies = []
    recommended_posters = []

    for idx in similar_indices:
        movie_id = movies.iloc[idx].movie_id
        recommended_movies.append(movies.iloc[idx].title)

        poster = fetch_poster(movie_id)
        recommended_posters.append(poster)

    return recommended_movies, recommended_posters

# ---------- STREAMLIT UI ----------
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox("Select a movie", movies_list)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            if posters[i]:
                st.image(posters[i], width=230)
            else:
                st.write("Poster not available")
            st.caption(names[i])

st.markdown(
    """
    <p style='text-align: center; color: gray;'>
    Developed by <b>Narpat Ganwliya</b> |
    <a href="https://www.linkedin.com/in/narpat-ganwliya/" target="_blank">LinkedIn</a> |
    <a href="https://github.com/narpatganwliya7" target="_blank">GitHub</a>
    </p>
    """,
    unsafe_allow_html=True
)
