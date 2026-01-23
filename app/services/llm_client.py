# OpenAI style
import os
import openai
from openai import OpenAI

# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
if not client.api_key:
    raise RuntimeError("OPENAI_API_KEY is not set")


def call_llm(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-5-nano",
        input=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        # temperature=0.3,
    )
    return response.output_text

