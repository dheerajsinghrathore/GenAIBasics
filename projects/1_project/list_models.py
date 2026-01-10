from dotenv import load_dotenv
from google import genai
import os

def list_models():
    load_dotenv()
    client = genai.Client()
    for model in client.models.list():
        print(f"Model: {model.name}, Supported Methods: {model.supported_actions}")

if __name__ == "__main__":
    list_models()
