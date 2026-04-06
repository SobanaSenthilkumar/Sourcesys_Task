from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "Deep learning models are powerful",
    "Neural networks can learn patterns",
    "Today the temperature is very high",
    "It is a hot summer day"
]

embeddings = model.encode(sentences)

print("===== SENTENCE EMBEDDINGS =====\n")

for i in range(len(sentences)):
    print(f"Sentence {i+1}: {sentences[i]}")
    print(f"Embedding (first 5 values): {embeddings[i][:5]}")
    print("-" * 50)

with open("embeddings_output.txt", "w") as f:
    f.write("===== SENTENCE EMBEDDINGS =====\n\n")
    
    for i in range(len(sentences)):
        f.write(f"Sentence {i+1}: {sentences[i]}\n")
        f.write(f"Embedding (first 5 values): {embeddings[i][:5]}\n")
        f.write("-" * 50 + "\n")

print("✅ Output saved to embeddings_output.txt")