import openai
from typing import List, Optional
from .base import BaseLLM

class OpenAILLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            **kwargs
        )
        return response.choices[0].message.content

    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        responses = [self.generate(prompt, **kwargs) for prompt in prompts]
        return responses

    def get_num_tokens(self, text: str) -> int:
        import tiktoken
        encoding = tiktoken.encoding_for_model(self.model)
        return len(encoding.encode(text))
