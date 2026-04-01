from transformers import pipeline

classifier = pipeline("text-classification")

text = "I love learning new technologies!"

result = classifier(text)

print("Input:", text)
print("Output:", result)