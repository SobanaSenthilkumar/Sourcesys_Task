from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\VICKY\OneDrive\Desktop\Sourcesys\Embedding\dataset.csv")
texts = df["text"].tolist()

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Convert to embeddings
embeddings = model.encode(texts).astype('float32')

# Normalize
faiss.normalize_L2(embeddings)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

# Add embeddings
index.add(embeddings)

print("✅ Vector database created!\n")

# User query
query = input("Enter your query: ")

# Encode query
query_vec = model.encode([query]).astype('float32')
faiss.normalize_L2(query_vec)

# Search
k = 3
scores, indices = index.search(query_vec, k)

print("\n===== SEARCH RESULTS =====\n")

with open("results.txt", "w") as f:
    f.write("===== VECTOR SEARCH RESULTS =====\n\n")
    f.write(f"Query: {query}\n\n")

    for rank, i in enumerate(indices[0]):
        sentence = texts[i]
        score = scores[0][rank]

        output = f"{rank+1}. {sentence}\n   Similarity Score: {score:.4f}\n\n"
        
        print(output)
        f.write(output)

print("✅ Results saved to results.txt")