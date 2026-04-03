from transformers import pipeline
from datasets import load_dataset

# Open file to save output
file = open("output.txt", "w", encoding="utf-8")

# Load dataset
dataset = load_dataset("ag_news")

sample_text = dataset["train"][0]["text"]

file.write("📌 SAMPLE TEXT:\n" + sample_text + "\n\n")

# -------------------------------
# PIPELINE 1: Text Classification
# -------------------------------
classifier = pipeline("text-classification")
result1 = classifier(sample_text)

file.write("✅ PIPELINE 1: TEXT CLASSIFICATION\n")
file.write(str(result1) + "\n\n")

# -------------------------------
# PIPELINE 2: Zero-Shot Classification
# -------------------------------
zero_shot = pipeline("zero-shot-classification")

labels = ["World", "Sports", "Business", "Technology"]

result2 = zero_shot(sample_text, candidate_labels=labels)

file.write("✅ PIPELINE 2: ZERO-SHOT CLASSIFICATION\n")
file.write(str(result2) + "\n\n")

# -------------------------------
# PIPELINE 3: NER
# -------------------------------
ner = pipeline("ner", grouped_entities=True)

result3 = ner(sample_text)

file.write("✅ PIPELINE 3: NER\n")
file.write(str(result3) + "\n\n")

# -------------------------------
# PIPELINE 4: Text Generation
# -------------------------------
generator = pipeline("text-generation", model="gpt2")

result4 = generator(sample_text, max_length=50, num_return_sequences=1)

file.write("✅ PIPELINE 4: TEXT GENERATION\n")
file.write(result4[0]['generated_text'] + "\n\n")

# -------------------------------
# PIPELINE 5: Summarization
# -------------------------------
summarizer = pipeline(
    "text2text-generation",
    model="sshleifer/distilbart-cnn-12-6"
)

long_text = sample_text * 5

result5 = summarizer(long_text, max_length=50, min_length=20, do_sample=False)

file.write("✅ PIPELINE 5: SUMMARIZATION\n")
file.write(result5[0]['generated_text'] + "\n\n")

# Close file
file.close()

print("✅ All outputs saved to output.txt")