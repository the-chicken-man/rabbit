import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")  

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    

    response = openai.Completion.create(
        model="gpt-4.0",  
        prompt=user_message,
        max_tokens=150
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(debug=True)
