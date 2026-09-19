import json
import math
from core.core import optimizer

prompts_tested = 0
token_start = 0
optimized_tokens = 0
tokens_saved = 0
Overall_reduction = 0

with open('prompts.json') as f:
    prompts = json.load(f)
for prompt in prompts:
    current_obj = optimizer(prompt)
    prompts_tested += 1
    token_start += current_obj.raw_text_token_count
    optimized_tokens += current_obj.final_prompt_token_count
    tokens_saved += current_obj.tokens_saved
    overall_reduction = math.ceil((1 - optimized_tokens/token_start) * 100)
print("Prompts Tested :" ,prompts_tested)
print("Original Tokens Used: ",token_start)
print("Amount of Tokens Used Post Optimization: ",optimized_tokens)
print("Total tokens saved: ",tokens_saved)
print("% reduction of tokens: ",overall_reduction, "%")