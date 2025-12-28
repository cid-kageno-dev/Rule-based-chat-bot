import random
from chatbot.responses import responses, default_responses

def get_response(user_input: str) -> str:
    user_input = user_input.lower().split()

    for keyword, replies in responses.items():
        if keyword in user_input:
            return random.choice(replies)

    return random.choice(default_responses)
