import re
from dataclasses import dataclass
from tokenCounter import tokenCount

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
    optimizedPrompt = re.sub(r"\bplease\b", "", optimizedPrompt, flags =re.IGNORECASE)
    optimizedPrompt = re.sub(r"\bI would like you to\b", "", optimizedPrompt, flags =re.IGNORECASE)
    optimizedPrompt = re.sub(r"\bcould you\b", "", optimizedPrompt, flags =re.IGNORECASE)
    optimizedPrompt = optimizedPrompt.strip()

    final_prompt_token_count = tokenCount(optimizedPrompt)
    tokens_saved = raw_text_token_count - final_prompt_token_count
    reduction_in_tokens = (tokens_saved / raw_text_token_count) * 100
    optimizedPromptOBJ = Veloce(optimizedPrompt, raw_text_token_count, final_prompt_token_count, tokens_saved, reduction_in_tokens)

    return optimizedPromptOBJ

test1 = optimizer("I would     like you     to     please build a     calculator")

print(test1.raw_text_token_count)
print(test1.tokens_saved)
