from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from chat import chatbot

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/ask", methods=['POST'])
def ask():
    data = request.get_json()
    message = data['messageText']

    # Handle the grammar correction
    #corrected_text = TextBlob(message)
    #print("CT:", corrected_text.correct())
    bot_response = chatbot(str(message))

    return jsonify({'status': 'OK', 'answer': bot_response})



if __name__ == "__main__":
    app.run()