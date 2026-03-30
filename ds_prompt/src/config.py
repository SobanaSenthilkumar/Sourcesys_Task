import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_client():
    return client