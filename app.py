from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS
import nltk
import os

# Setup NLTK data path
NLTK_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(NLTK_PATH, exist_ok=True)
nltk.data.path.append(NLTK_PATH)

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=NLTK_PATH)

# Initialize Flask
app = Flask(__name__)
CORS(app, origins=["https://lunas-portfolio.vercel.app"], methods=["POST"], allow_headers=["Content-Type"])

# ✅ Handle OPTIONS requests manually
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = None
        if 'ACCESS_CONTROL_REQUEST_HEADERS' in request.headers:
            headers = request.headers['ACCESS_CONTROL_REQUEST_HEADERS']
        h = response.headers

        h['Access-Control-Allow-Origin'] = 'https://lunas-portfolio.vercel.app'
        h['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        h['Access-Control-Allow-Headers'] = headers or 'Content-Type'
        return response

# Route: Chat API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"response": "Please send a message."})

    response = get_response(message)
    return jsonify({"response": response})

# Route: Health check
@app.route("/health")
def health():
    return "OK"

# Run with waitress in production
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
