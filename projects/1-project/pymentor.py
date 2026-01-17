from openai import OpenAI
from dotenv import load_dotenv
import os


def get_openai_client():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")
    client = OpenAI(api_key=api_key)
    return client


def chat_with_mentor(client, question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful coding mentor. Provide concise and accurate explanations."},
                {"role": "user", "content": question}
            ]
        )
        print("\nMentor's Response:", response.choices[0].message.content)
    except Exception as e:
        print(f"\nError in chat: {e}")


try:
    client = get_openai_client()
    print("Mentor is ready! Type 'exit' to quit.")
    while True:
        user_question = input("\nAsk your coding question (or type 'exit' to quit): ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        if not user_question.strip():
            continue
        chat_with_mentor(client, user_question)
except Exception as e:
    print("An error occurred:", str(e))