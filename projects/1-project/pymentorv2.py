from openai import OpenAI
from dotenv import load_dotenv


def get_open_ai_client():
    load_dotenv()
    return OpenAI()


def chat_with_ai(messages):
    response = client.responses.create(model="gpt-5.1", input=messages)
    return response.output_text


try:
    client = get_open_ai_client()
    messages = [
        {
            "role": "system",
            "content": "You are a helpful Python tutor. Please answer questions related to Python only in a concise way. For any other question DO NOT ANSWER and give a polite reply",
        }
    ]
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        messages.append({"role": "user", "content": user_input})
        ai_response = chat_with_ai(messages)
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})
except Exception as ex:
    print("Error", ex)
