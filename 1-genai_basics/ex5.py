from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()   # Initialize the OpenAI client automatically using the API key from the .env file
response = client.responses.create(
    model="gpt-4.1-mini", input="What is capital of India?"
)
print(response.output_text)
