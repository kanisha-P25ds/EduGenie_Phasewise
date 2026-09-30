from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# Load the lightweight local model used for explanations
MODEL_NAME = "MBZUAI/LaMini-Flan-T5-783M"

explain_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

explain_model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def explain_topic(topic: str) -> str:

    if not topic or not topic.strip():
        return "⚠ Please provide a topic."

    input_text = (
        f"Explain the concept of '{topic}' "
        "in a simple and clear way for a school student."
    )

    inputs = explain_tokenizer(
        input_text,
        return_tensors="pt"
    )

    outputs = explain_model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        do_sample=True
    )

    explanation = explain_tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return explanation