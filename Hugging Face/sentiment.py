from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = "This movie is amazing!"
result = classifier(text)

print("Input:", text)
print("Output:", result)