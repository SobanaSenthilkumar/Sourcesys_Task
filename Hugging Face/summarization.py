from transformers import pipeline

generator = pipeline("text-generation")

text = "Artificial Intelligence is transforming industries by automating tasks, improving efficiency, and enabling new innovations."

prompt = "Summarize this: " + text

result = generator(prompt, max_length=50)

print(result[0]["generated_text"])