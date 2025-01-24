import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
# print(google_api_key)

## llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key=google_api_key)
llm=genai.GenerativeModel('gemini-1.5-pro-latest')

st.set_page_config(page_title="Chatbot Text Demo",page_icon=":robot:")
st.title("Chatbot Text")
st.sidebar.header("Chatbot Text Demo")

st.divider()


query=st.text_input('Enter your Query here....')

if st.button('Submit'):
    User = 'User'
    Chatbot = 'Chatbot' 

    st.write(f'{User} - {query}')
    response =llm.invoke(query)
    st.write(f'{Chatbot} - {response.content}')
