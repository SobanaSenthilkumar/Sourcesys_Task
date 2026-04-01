from transformers import pipeline

generator = pipeline("text-generation")

text = "Machine learning is amazing"

prompt = "Translate English to French: " + text

result = generator(prompt, max_length=50)

print(result[0]["generated_text"])