import os
import time

from dotenv import load_dotenv
import google.generativeai as genai


# Load .env file
load_dotenv()


# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. "
        "Check that your .env file exists and contains GEMINI_API_KEY."
    )


# Configure Gemini
genai.configure(api_key=api_key)

MODEL_NAME = "gemini-3.5-flash"


def generate_text(prompt: str, retries: int = 2) -> str:

    model = genai.GenerativeModel(MODEL_NAME)

    for attempt in range(retries + 1):

        try:
            response = model.generate_content(prompt)

            if not response or not response.text:
                return "⚠ Gemini returned an empty response."

            return response.text.strip()

        except Exception as e:

            error = str(e)

            if (
                "429" in error
                or "RESOURCE_EXHAUSTED" in error
                or "quota" in error.lower()
            ):

                if attempt >= retries:
                    return (
                        "⚠ Gemini API quota has been exceeded. "
                        "Please try again after the quota resets."
                    )

                wait_time = 2 ** attempt
                time.sleep(wait_time)

            else:
                return f"⚠ Gemini error: {error}"

    return "⚠ Gemini request failed."