# jarvis_brain.py - Ubongo utakaopanda Render
from flask import Flask, request
import requests

app = Flask(__name__)

# WEKA IP ZA AGENT ZAKO HAPA
AGENT_LAPTOP = "http://192.168.10.111:5001" # Badili hii kama IP yako itabadilika
AGENT_TABLET = "http://IP_YA_TABLET:5002" # Tutaijua baada ya kuiwasha Tablet

@app.route("/")
def home():
    return "Jarvis Brain yuko Cloud. Tayari kupokea amri"

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    message = request.form.get('Body', '').lower()
    reply = "Samahani boss sijaelewa amri"

    try:
        if "laptop" in message:
            if "fungua" in message:
                requests.get(f"{AGENT_LAPTOP}/command?cmd={message}")
                reply = f"Nimetuma amri kwenda Laptop: {message}"

            elif "tuma" in message and "kwenda tablet" in message:
                file_name = message.split('"')[1] # Jarvis tuma "file.pdf" kwenda tablet
                requests.get(f"{AGENT_LAPTOP}/send_file?name={file_name}")
                reply = f"Nimeanza kutuma {file_name} kutoka Laptop"

        elif "tablet" in message:
            requests.get(f"{AGENT_TABLET}/command?cmd={message}")
            reply = f"Nimetuma amri kwenda Tablet: {message}"

    except Exception as e:
        reply = f"Kuna shida boss: {e}. Hakikisha Agent yuko hai"

    return reply # Hii ndio WhatsApp itakujibu

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)