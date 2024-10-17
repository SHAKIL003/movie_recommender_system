import streamlit as st
import pickle
import pandas as pd

# Load movie data as DataFrame
movies_df = pd.read_pickle('movies.pkl')

# Extract movie titles
movies_listed = movies_df['title'].values

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list1:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_listed)

if st.button('Recommend'):
    st.write(selected_movie_name)
    recommendation = recommend(selected_movie_name)
    for movie in recommendation:
        st.write(movie)
else:
    st.write('Goodbye!')

#### Old Code


# import streamlit as st
# import pickle
# import pandas as pd

# movies_list = pickle.load(open('movies.pkl', 'rb'))
# movies_listed = movies_list['title'].values

# similarity = pickle.load(open('similarity.pkl', 'rb'))

# st.title("Movie Recommendation System NEU")


# def recommend(movie):
#   movie_index = movies_list[movies_list['title'] == movie].index[0]
#   distances = similarity[movie_index]
#   movies_list1 = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]

#   recommended_movies = []
#   for i in movies_list1:
#     recommended_movies.append(movies_list.iloc[i[0]].title)
#   return recommended_movies

# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     movies_listed)

# #st.button("Reset", type="primary")
# if st.button('Recommend'):
#     st.write(selected_movie_name)
#     recommendation = recommend(selected_movie_name)
#     for i in recommendation:
#         st.write(i)
# else:
#     st.write('Goodbye')
