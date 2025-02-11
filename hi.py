from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway assigns PORT dynamically
    app.run(debug=True, host="0.0.0.0", port=port)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up Gemini API
genai.configure(api_key=os.getenv("AIzaSyCY3ME1xdj5q1_-m7umKHG1OJh2e8Nmie0



"))
if not API_KEY:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)

def chatbot_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text if response else "Sorry, I couldn't process that."
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.get_json()  # Ensure Flask reads JSON data
    user_input = data.get('user_input', '')  # Extract input
    response = chatbot_response(user_input)
    return jsonify({"response": response})


    
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)


