from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:

    if not topic or not topic.strip():
        return "⚠ Please provide a topic."

    prompt = f"""
You are an AI tutor.

The student wants to learn about:

{topic}

Create a structured learning path.

Include:

1. Beginner topics
2. Intermediate topics
3. Advanced topics when appropriate
4. Recommended order of learning
5. Useful resources such as videos, articles, and books

Keep the explanation clear, practical, and easy for a student to follow.
"""

    return generate_text(prompt)