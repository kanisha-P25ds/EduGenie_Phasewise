from gemini_client import generate_text


def summarize_text(text: str) -> str:

    if not text or not text.strip():
        return "⚠ Please provide some text to summarize."

    prompt = f"""
You are an AI tutor.

Summarize the following text in simple and clear language.

Keep the important points.

Text:

{text}
"""

    return generate_text(prompt)
