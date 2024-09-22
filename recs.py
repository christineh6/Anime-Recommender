import pandas as pd # type: ignore

# Load the dataset
anime_df = pd.read_csv('data/anime.csv')

# Inspect the dataset
print(anime_df.head())

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Preprocess genres (clean any missing or inconsistent data)
anime_df['Genres'] = anime_df['Genres'].fillna('')

# Convert genres into a matrix of TF-IDF features
tfidf = TfidfVectorizer(stop_words='english')
genre_matrix = tfidf.fit_transform(anime_df['Genres'])

# Calculate cosine similarity between all anime
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = anime_df[anime_df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 recommendations
    anime_indices = [i[0] for i in sim_scores]
    return anime_df['Title'].iloc[anime_indices]

# Test with a sample anime
print(get_recommendations('Naruto'))
