import pandas as pd #type: ignore

anime_df = pd.read_csv('data/anime.csv')

#tester statement1
print(anime_df.head())

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#preprocess genres (clean any missing or inconsistent data)
anime_df['genre'] = anime_df['genre'].fillna('')

#converting genres into a matrix of TF-IDF features
tfidf = TfidfVectorizer(stop_words='english')
genre_matrix = tfidf.fit_transform(anime_df['genre'])

#cosine similarity between all anime
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

#function to get recommendations
def get_recommendations(name, cosine_sim=cosine_sim):
    idx = anime_df[anime_df['name'] == name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # top 10 recommendations
    anime_indices = [i[0] for i in sim_scores]
    return anime_df['name'].iloc[anime_indices]

#tester
print(get_recommendations('Naruto'))
