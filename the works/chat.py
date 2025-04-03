import openai
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify

load_dotenv()  # Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# This function will handle POST requests to '/api/chat'
def handler(req, res):
    try:
        data = req.json
        prompt = data.get("prompt")
        ai_response = chat_with_ai(prompt)
        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
