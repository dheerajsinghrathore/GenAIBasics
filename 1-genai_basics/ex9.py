from openai import OpenAI
from dotenv import load_dotenv

def get_openai_client():
    load_dotenv()
    import os
    api_key = os.getenv("OPENAI_API_KEY")
    return


