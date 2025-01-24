import os
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_community.chat_models import ChatGooglepalm
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
print(google_api_key)

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=google_api_key)

## query = "what is the capital of india?"

while True:
    print('#'*60)
    query = input("Enter the Query:")
    result=llm.invoke(query)
    print(result.content)
    print('#'*60)

