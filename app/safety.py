BANNED_KEYWORDS = [
    "buy", "sell", "invest in", "best stock",
    "intraday", "tomorrow", "target price",
    "guaranteed", "profit", "returns"
]

def is_advice_request(text: str) -> bool:
    text = text.lower()
    return any(word in text for word in BANNED_KEYWORDS)


REFUSAL_MESSAGE = (
    "I can’t help with stock recommendations or investment advice.\n\n"
    "I *can* help you learn investing concepts and evaluation frameworks.\n\n"
    "Educational purposes only."
)
