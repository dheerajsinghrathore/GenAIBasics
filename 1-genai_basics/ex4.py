from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
my_api_key = os.getenv("GEMINI_API_KEY")

if not my_api_key:
    raise ValueError("GEMINI_API_KEY is not set in environment variables.")
else:
    client = genai.Client(api_key=my_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Who is prime minister of India?"
    )
    print(response.text)
