import os
from openai import OpenAI


def generate_text(text: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is missing")

    client = OpenAI(
        api_key=api_key,
        timeout=60.0,
        max_retries=5,
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=(
            "Ты помощник для создания карточек товаров. "
            "По описанию товара создай короткий привлекательный текст "
            "на русском языке: название, описание и 3 преимущества.\n\n"
            f"Товар: {text}"
        ),
    )

    return response.output_text
