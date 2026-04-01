from transformers import pipeline

generator = pipeline("text-generation")

text = "Artificial Intelligence is"

result = generator(text, max_length=30)

print("Input:", text)
print("Output:", result[0]["generated_text"])