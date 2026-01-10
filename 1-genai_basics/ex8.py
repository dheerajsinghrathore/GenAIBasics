from openai import OpenAI
import os
from dotenv import load_dotenv

def get_openai_client():
    load_dotenv()
    client = OpenAI()
    return client

def chat_with_openai(prompt):
    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
