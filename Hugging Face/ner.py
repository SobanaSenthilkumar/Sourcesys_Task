from transformers import pipeline

ner = pipeline("ner", aggregation_strategy="simple")

text = "Sundar Pichai is the CEO of Google and lives in the USA."
result = ner(text)

print("Input:", text)
print("Output:", result)