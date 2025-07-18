from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

gemini_llm = ChatGoogleGenerativeAI(
model="gemini-2.5-pro"
)
chat_gpt_llm=ChatOpenAI(model='gpt-4.1-mini-2025-04-14')


def get_model():
    model = gemini_llm
    return model
 