import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances


# ------------------------------
# Sample Documents
# ------------------------------
documents = [
    "I love machine learning",
    "Machine learning is powerful",
    "I enjoy deep learning",
    "Python is great for AI"
]

# ------------------------------
# Vectorization (Bag of Words)
# ------------------------------
vectorizer = CountVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

# ------------------------------
# Input Query
# ------------------------------
query = input("Enter search query: ")
query_vector = vectorizer.transform([query])


# ------------------------------
# 1️⃣ Cosine Similarity
# ------------------------------
cos_sim = cosine_similarity(query_vector, doc_vectors)

print("\nCosine Similarity Scores:")
for i, score in enumerate(cos_sim[0]):
    print(f"Doc {i+1}: {score:.4f}")


# ------------------------------
# 2️⃣ Euclidean Distance
# ------------------------------
euclidean = pairwise_distances(query_vector, doc_vectors, metric='euclidean')

print("\nEuclidean Distance Scores (Lower is Better):")
for i, score in enumerate(euclidean[0]):
    print(f"Doc {i+1}: {score:.4f}")


# ------------------------------
# 3️⃣ Dot Product
# ------------------------------
dot_product = np.dot(query_vector.toarray(), doc_vectors.toarray().T)

print("\nDot Product Scores:")
for i, score in enumerate(dot_product[0]):
    print(f"Doc {i+1}: {score:.4f}")


# ------------------------------
# 4️⃣ Jaccard Similarity
# ------------------------------
def jaccard_similarity(str1, str2):
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())
    return len(set1 & set2) / len(set1 | set2)

print("\nJaccard Similarity Scores:")
for i, doc in enumerate(documents):
    score = jaccard_similarity(query, doc)
    print(f"Doc {i+1}: {score:.4f}")