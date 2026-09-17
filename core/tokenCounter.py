import tiktoken as tik

def tokenCount(text):
    encoding = tik.get_encoding("o200k_base")
    tokenNum = len(encoding.encode(text))
    return tokenNum


