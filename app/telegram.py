import requests
import os
from dotenv import load_dotenv
from app.router import handle_message

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

user_modes = {}

def send_message(chat_id: int, text: str):
    requests.post(
        f"{TELEGRAM_API}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

def handle_telegram_update(update: dict):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    # Start command
    if text == "/start":
        user_modes[chat_id] = "coach"
        send_message(
            chat_id,
            (
                "👋 Hi! I’m *InvestMentor*.\n\n"
                "I can:\n"
                "📘 Teach investing concepts\n"
                "📰 Explain market news\n\n"
                "⚠️ Educational purposes only.\n\n"
                "Commands:\n"
                "/coach – Learn investing\n"
                "/market – Market commentary"
            )
        )
        return

    # Mode switch
    if text == "/coach":
        user_modes[chat_id] = "coach"
        send_message(chat_id, "📘 Switched to Investment Coach mode.")
        return

    if text == "/market":
        user_modes[chat_id] = "market"
        send_message(chat_id, "📰 Switched to Market Commentary mode.")
        return

    mode = user_modes.get(chat_id, "coach")
    response = handle_message(text, mode)
    send_message(chat_id, response)
