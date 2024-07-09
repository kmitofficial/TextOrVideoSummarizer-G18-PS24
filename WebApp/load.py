import google.generativeai as genai
import os
from dotenv import load_dotenv
def output(text):
    response = model.generate_content("Summarize this and also don't make this too short "+text)
    return response
load_dotenv()
GOOGLE_API_KEY = os.getenv("API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')