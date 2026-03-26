import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🤖 AI Chatbot")


if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])


user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").markdown(user_input)

    response = st.session_state.chat.send_message(user_input)

    st.chat_message("assistant").markdown(response.text)