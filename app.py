from flask import Flask, request, jsonify
from chat import get_response  # your chatbot function
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    if not message:
        return jsonify({"response": "Please send a message."})

    response = get_response(message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # runs on http://localhost:5000
