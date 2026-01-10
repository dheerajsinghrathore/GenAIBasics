from dotenv import load_dotenv
from google import genai
from google.genai import types


def get_gemini_ai_client():
    load_dotenv()
    return genai.Client()

def chat_with_ai(content_list):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        config=types.GenerateContentConfig(
            system_instruction=("You are a helpful Python tutor")
        ),
        contents=content_list,
    )
    return response.text


try:
    content_list = []
    client = get_gemini_ai_client()
    print("I am a Python Tutor")
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        content_list.append(
            types.Content(role="user", parts=[types.Part(text=user_input)])
        )
        ai_reply = chat_with_ai(content_list)
        print("AI:", ai_reply)
        content_list.append(
            types.Content(role="model", parts=[types.Part(text=ai_reply)])
        )
except Exception as ex:
    print("Error:", ex)
