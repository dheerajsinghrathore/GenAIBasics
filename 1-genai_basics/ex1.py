from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini", input="Hello, I am Dheeraj. What about you?"
)

print(response.output_text)
