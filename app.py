import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatGooglepalm
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
# print(google_api_key)

llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key=google_api_key)

st.set_page_config('Chatbot Application',layout='centered')
st.title('Chatbot Application')
st.divider()


query=st.text_input('Enter your Query here....')

if st.button('Submit'):
    User = 'User'
    Chatbot = 'Chatbot' 

    st.write(f'{User} - {query}')
    response =llm.invoke(query)
    st.write(f'{Chatbot} - {response.content}')


# query=st.chat_input('Enter your Query here....')
 
#User = 'User'
#Chatbot = 'Chatbot' 

#if query:
    #st.chat_message(User).write(query)
   # response =llm.invoke(query)   
    #st.chat_message('Chatbot').write(response.content)
    