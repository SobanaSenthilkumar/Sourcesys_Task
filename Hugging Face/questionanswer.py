from transformers import pipeline

qa = pipeline("question-answering")

context = "Hugging Face develops tools for natural language processing."
question = "What does Hugging Face develop?"

result = qa(question=question, context=context)

print("Question:", question)
print("Answer:", result)