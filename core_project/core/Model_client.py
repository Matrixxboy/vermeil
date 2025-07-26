import requests
from Model.model_config import OLLAMA_URL, OLLAMA_MODEL

def query_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "").strip()
