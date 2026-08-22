from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Hapa weka Token yako ya Twilio baadaye
TWILIO_TOKEN = "weka_token_yako_hapa"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Jarvis Brain is Running ✅"})

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')
    
    # Jibu rahisi la Jarvis
    if "hi" in incoming_msg or "hello" in incoming_msg:
        reply = "Habari mkuu! Mimi ni Jarvis. Nipo tayari kukusaidia 😎"
    elif "help" in incoming_msg:
        reply = "Unaweza kuniuliza lolote. Jaribu kuniambia 'weather' au 'time'"
    else:
        reply = f"Nimesikia: {incoming_msg}. Bado ninajifunza kujibu vizuri 😅"

    return reply, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
