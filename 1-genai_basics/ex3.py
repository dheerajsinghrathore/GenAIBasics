from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")
if my_api_key is None:
    raise ValueError(
        "API key not found. Please set the OPENAI_API_KEY environment variable."
    )
else:
    client = OpenAI(api_key=my_api_key)
    response = client.responses.create(
        model="gpt-4.1-mini", input="What is capital of India?"
    )
    print(response.output_text)
