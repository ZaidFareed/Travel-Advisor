import openai
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the chatbot function
def chatbot(input):
    messages = [
        {"role": "system", "content": "You are an expert travel advisor. Help people plan their perfect vacation."}
    ]
    messages.append({"role": "user", "content": input})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    return reply

# Custom CSS to adjust styles and attempt to target the whole window
st.markdown("""
<style>
    /* Attempt to change the overall background */
    html, body, .stApp {
        background-color: #000000 !important;
    }
    /* Adjust text and elements for visibility against black background */
    .stTextInput>div>div>div>input, .st-bb, .st-at, .st-cf, .markdown-text-container {
        color: #000000; /* Bright green for visibility */
    }
    /* Specifically targeting user input to be black */
    .stTextInput>div>div>div>input {
        color: #000000; /* Black text for user input */
        background-color: #333; /* Darker elements background, adjust if needed */
        border-color: #4CAF50; /* Bright green border, maintain consistency */
    }
    .stTextArea>div>div>textarea, .stButton>button {
        background-color: #333; /* Darker elements background */
        color: #4CAF50; /* Keeping text green for text areas and buttons */
        border-color: #4CAF50; /* Bright green border */
    }
    .stButton>button:hover {
        background-color: #555; /* Lighter background on hover */
    }
    /* Adjusting heading sizes */
    h2 {
        font-size: 40px; /* Adjusted size for h2 */
    }
    h4 {
        font-size: 20px; /* Adjusted size for h4 */
    }s
</style>
""", unsafe_allow_html=True)

# Headers and user input
st.markdown("<h2 style='color: #4CAF50; margin-top: 0;'>AI Travel Advisor</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #4CAF50;'>Tell me about your travel plans:</h4>", unsafe_allow_html=True)  # Custom prompt with corrected CSS
# Adjusted user input with a label and hiding the label
user_input = st.text_input("Prompt", '', label_visibility="collapsed")

# Adjusted reply box with a label and hiding the label
if st.button("Submit"):
    reply = chatbot(user_input)
    if reply:
        st.text_area(label="Response", value=reply, height=150, key="reply_box", label_visibility="collapsed")

