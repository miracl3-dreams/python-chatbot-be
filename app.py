from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow your frontend domain
CORS(app, origins=["https://lunas-portfolio.vercel.app"])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({"response": "Please send a message."})

    response = get_response(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    # Use waitress in production if available, otherwise fallback to Flask
    if os.environ.get("FLASK_ENV") == "production":
        from waitress import serve
        serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        app.run(debug=True, port=5000)
