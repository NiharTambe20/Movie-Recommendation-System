import streamlit as st
import pickle
import pandas as pd
import requests


# TMDB API KEY
API_KEY = st.secrets["TMDB_API_KEY"]


# Fetch movie poster from TMDB API
def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

        return None

    except requests.exceptions.Timeout:
        return None

    except requests.exceptions.RequestException as e:
        st.warning(f"TMDB API Error: {e}")
        return None


# Recommendation Function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:

        # Get actual TMDB movie ID
        movie_id = movies.iloc[i[0]].movie_id

        # Fetch poster using actual movie ID
        poster = fetch_poster(movie_id)

        recommended_movies_posters.append(poster)

        # Get movie title
        recommended_movies.append(
            movies.iloc[i[0]]['title']
        )

    return recommended_movies, recommended_movies_posters


# Load Movie Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# Streamlit Application
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select an option',
    movies['title'].values
)


# Recommend Button
if st.button('Recommend'):

    names, posters = recommend(selected_movie_name)

    # Create 5 columns
    col = st.columns(5)

    # Display recommended movies
    for i in range(5):

        with col[i]:

            st.text(names[i])

            if posters[i] is not None:
                st.image(posters[i])
            else:
                st.write("Poster Not Available")