import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

print(chat_with_ai("Hello, Rabbit!"))
