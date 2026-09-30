import re
import json

from gemini_client import generate_text


def clean_json_block(text: str) -> str:
    """
    Remove Markdown JSON code fences if Gemini adds them.
    """

    return re.sub(
        r"```(?:json)?\s*(.*?)```",
        r"\1",
        text,
        flags=re.DOTALL
    ).strip()


def generate_quiz(text: str) -> list:

    if not text or not text.strip():
        return [
            {
                "error": "⚠ Please provide some text for the quiz."
            }
        ]

    prompt = f"""
You are an AI quiz generator.

From the following passage, create exactly 3 multiple-choice questions.

Each question must contain:

- "question"
- "options": exactly 4 options
- "answer": the correct answer

The answer must exactly match one of the options.

Return ONLY valid JSON.

Do not include explanations.
Do not include Markdown.
Do not include ```json.

Example:

[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:

{text}
"""

    try:

        quiz_text = generate_text(prompt)

        # Gemini helper returned an error
        if quiz_text.startswith("⚠"):
            return [
                {
                    "error": quiz_text
                }
            ]

        cleaned_text = clean_json_block(quiz_text)

        quiz_list = json.loads(cleaned_text)

        # Make sure Gemini actually returned a list
        if not isinstance(quiz_list, list):
            return [
                {
                    "error": "⚠ Gemini did not return a valid quiz list."
                }
            ]

        return quiz_list

    except json.JSONDecodeError as e:

        return [
            {
                "error": f"⚠ Could not parse quiz JSON: {e}"
            }
        ]

    except Exception as e:

        return [
            {
                "error": f"⚠ Error generating quiz: {e}"
            }
        ]
