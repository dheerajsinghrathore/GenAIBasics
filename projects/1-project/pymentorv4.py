from openai import OpenAI
from dotenv import load_dotenv
import json
import os

CHAT_FILE = "chat_history.json"


def get_open_ai_client():
    load_dotenv()
    return OpenAI()


def chat_with_ai(messages):
    response = client.responses.create(model="gpt-5.1", input=messages)
    return response.output_text


def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as file_obj:
            return json.load(file_obj), False
    else:
        messages = [
            {
                "role": "system",
                "content": (
                    "You are PyMentor, a Python tutor. "
                    "You must answer only Python related questions."
                    "If the user asks anything else not related to Python."
                    "do not answer at all and politely refuse"
                ),
            }
        ]
        return messages, True


def save_chat_history(messages):
    with open(CHAT_FILE, "w") as file_obj:
        json.dump(messages, file_obj, indent=4)


try:
    client = get_open_ai_client()
    messages, is_new_chat = load_chat_history()
    if is_new_chat:
        print("WELCOME TO PYMENTOR-Your AI Python Tutor")
        print("You can ask me anything related to Python")
        print("Type exit anytime to save the chat and leave")
    else:
        print("Chat resumed! Type exit to quit")
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            save_chat_history(messages)
            print("Chat saved. Good bye!")
            break
        messages.append({"role": "user", "content": user_input})
        ai_response = chat_with_ai(messages)
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})
except Exception as ex:
    print("Error", ex)
