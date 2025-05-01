import os
from openai import OpenAI


# Initialize OpenAI client
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("Missing OPENAI_API_KEY environment variable")

client = OpenAI(api_key=key)