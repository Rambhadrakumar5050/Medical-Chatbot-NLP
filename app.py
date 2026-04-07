from flask import Flask, render_template, request, jsonify
from model import chatbot_response

app = Flask(__name__)

# ✅ THIS IS IMPORTANT (HOME PAGE)
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    bot_reply = chatbot_response(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)