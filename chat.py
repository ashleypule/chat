import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

# Load the API key
groq_api_key = os.getenv('GROQ_API_KEY', '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')

# Initialize Groq client
client = Groq(api_key=groq_api_key)

# Set page configuration
st.set_page_config(page_title="StudGPT", page_icon="pic.png")


st.title("Find Your Answer")

st.image(image="pic.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# Chat interface
question = st.text_input("Ask me anything:")


# Create chat completion request
start = time.process_time()
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ],
    model="llama3-8b-8192",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
)

st.write("Answer:", chat_completion.choices[0].message.content)
