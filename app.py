from flask import Flask, render_template, request, jsonify
from config import Config
from models import get_openai_response

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def api_chat():
    user_message = request.json.get('message')
    response = get_openai_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
