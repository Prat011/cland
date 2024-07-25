import openai
from typing import List, Optional
from .base import BaseLLM

class OpenAILLM(BaseLLM):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str, **kwargs) -> str:
        response = openai.Completion.create(
            api_key=self.api_key,
            model=self.model,
            prompt=prompt,
            **kwargs
        )
        return response.choices[0].text

    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        responses = []
        for prompt in prompts:
            response = self.generate(prompt, **kwargs)
            responses.append(response)
        return responses

    def get_num_tokens(self, text: str) -> int:
        response = openai.Completion.create(
            api_key=self.api_key,
            model=self.model,
            prompt=text,
            max_tokens=0,
            logprobs=1
        )
        return response.choices[0].logprobs.token_logprobs[-1]
