# MODIFIED BY CS4371
import ollama


def chat_completion(text: str, model: str = "llama3.2") -> str:
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": text},
        ],
    )
    return response.message.content  # type: ignore
