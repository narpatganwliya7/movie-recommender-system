import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# Load cleaned movies data
movies = pickle.load(open('../models/movies.pkl', 'rb'))

# Vectorize movie tags
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vectors)

# Store only top 5 similar movies per movie (memory optimized)
top_similar = {}

for idx, row in enumerate(similarity):
    top_indices = sorted(
        list(enumerate(row)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]
    top_similar[idx] = top_indices

# Save optimized similarity object
with open('../models/top_similar.pkl', 'wb') as f:
    pickle.dump(top_similar, f)

print("✅ top_similar.pkl created successfully")
