from gemini_client import generate_text


def answer_question_with_gemini(question: str) -> str:

    if not question or not question.strip():
        return "⚠ Please enter a question."

    prompt = f"""
You are EduGenie, an AI learning assistant.

Answer the student's question clearly and accurately.

Use simple language that is appropriate for a school student.

Question:
{question}
"""

    return generate_text(prompt)