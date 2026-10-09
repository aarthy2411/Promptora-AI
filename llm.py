import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-3.8-flash"


def generate_response(prompt, temperature=0.2, max_tokens=500):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please check your .env file."
        )

    client = genai.Client(api_key=api_key)

    response = client.interactions.create(
        model=MODEL,
        input=prompt,
        generation_config={
            "temperature": temperature,
            "max_output_tokens": max_tokens
        }
    )

    answer = response.output_text

    if not answer:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return answer
