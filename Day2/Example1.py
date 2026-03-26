import numpy as np

# Vectors
u = np.array([5, 1, -2])
m1 = np.array([4, 0, 0])
m2 = np.array([1, 5, 4])

# Function for cosine similarity
def cosine_similarity(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    
    return dot_product / (norm_a * norm_b)

# Results
sim_m1 = cosine_similarity(u, m1)
sim_m2 = cosine_similarity(u, m2)

print("Cosine Similarity with m1:", sim_m1)
print("Cosine Similarity with m2:", sim_m2)