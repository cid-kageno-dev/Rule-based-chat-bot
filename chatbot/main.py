from chatbot.engine import get_response

def start_chatbot():
    print("Welcome! Simple rule-based chatbot.")
    print("Type 'bye' or 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("bye", "quit"):
            print("ChatBot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chatbot()
