from transformers import pipeline

fill_mask = pipeline("fill-mask")

text = "Machine learning is [MASK]."

result = fill_mask(text)

print("Input:", text)
print("Top Predictions:")
for r in result:
    print(r["sequence"], " | Score:", r["score"])