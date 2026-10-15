from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
api_key= os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

st.title("Talk to Chatbot")
st.write("This app demonstrates a conversational agent.")

user_input = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-flash-lite-latest', contents=user_input,
        )
    st.write(response.text)
