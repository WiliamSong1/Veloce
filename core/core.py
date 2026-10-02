import re
from dataclasses import dataclass
from .tokenCounter import tokenCount
from .rules import removal_rules, compression_rules


@dataclass
class Veloce:
    optmizedPrompt: str
    raw_text_token_count: int
    final_prompt_token_count: int
    tokens_saved: int
    reduction_in_tokens: float

def optimizer(prompt):
    if prompt == "":
        return
    raw_text_token_count = tokenCount(prompt)

    optimizedPrompt = prompt
    optimizedPrompt = re.sub(r"\s{2,}", " ", optimizedPrompt)

    for key, value in removal_rules.items():
        pattern = re.escape(key)
        optimizedPrompt = re.sub(pattern, value, optimizedPrompt, flags=re.IGNORECASE)
    for key, value in compression_rules.items():
        pattern = re.escape(key)
        optimizedPrompt = re.sub(pattern, value, optimizedPrompt, flags=re.IGNORECASE)
    optimizedPrompt = optimizedPrompt.strip()

    optimizedPrompt = clean_abandoned_punct(optimizedPrompt)

    final_prompt_token_count = tokenCount(optimizedPrompt)
    tokens_saved = raw_text_token_count - final_prompt_token_count
    reduction_in_tokens = (tokens_saved / raw_text_token_count) * 100
    optimizedPromptOBJ = Veloce(optimizedPrompt, raw_text_token_count, final_prompt_token_count, tokens_saved, reduction_in_tokens)

    return optimizedPromptOBJ


def clean_abandoned_punct(prompt):
    prompt = re.sub(r",\s*,", ",", prompt)
    prompt = re.sub(r"^,\s*", "", prompt)
    return prompt




