import argparse
from core.core import optimizer

parser = argparse.ArgumentParser(description = "Optimizer")

parser.add_argument("input" , type = str, help = "The input that you would like optimize for token usage")

args = parser.parse_args()

result = optimizer(args.input)

print(result.optmizedPrompt)
print("Original Tokens Used: ",result.raw_text_token_count)
print("Amount of Tokens Used Post Optimization: ",result.final_prompt_token_count)
print("Total tokens saved: ",result.tokens_saved)
print("% reduction of tokens: ",result.reduction_in_tokens, "%")