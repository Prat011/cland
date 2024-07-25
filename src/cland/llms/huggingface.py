from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List, Optional
from .base import BaseLLM

class HuggingFaceLLM(BaseLLM):
    def __init__(self, model_name: str = "gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate(self, prompt: str, **kwargs) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, **kwargs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def batch_generate(self, prompts: List[str], **kwargs) -> List[str]:
        responses = [self.generate(prompt, **kwargs) for prompt in prompts]
        return responses

    def get_num_tokens(self, text: str) -> int:
        return len(self.tokenizer.encode(text))
