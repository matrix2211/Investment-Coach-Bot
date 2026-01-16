from app.safety import is_advice_request, REFUSAL_MESSAGE
from app.llm.client import generate_response
from app.prompts.coach import COACH_PROMPT
from app.prompts.market import MARKET_PROMPT

def handle_message(text: str, mode: str = "coach") -> str:
    if is_advice_request(text):
        return REFUSAL_MESSAGE

    base_prompt = COACH_PROMPT if mode == "coach" else MARKET_PROMPT
    final_prompt = f"{base_prompt}\n\nUser: {text}"
    return generate_response(final_prompt)
