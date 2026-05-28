import requests


OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"


def ask_ollama(prompt: str, model: str = "qwen3:0.6b") -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
    }

    try:
        response = requests.post(OLLAMA_CHAT_URL, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        return f"调用 Ollama 失败：{error}"

    return response.json()["message"]["content"]
