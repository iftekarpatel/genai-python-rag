from openai import OpenAI
from config import GITHUB_TOKEN, MODEL_NAME, GITHUB_ENDPOINT


class AIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=GITHUB_TOKEN,
            base_url=GITHUB_ENDPOINT
        )
        self.model = MODEL_NAME

    def chat(self, messages, temperature=0.7, stream=False):
        if stream:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream=True
            )
        else:
            return self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature
            )