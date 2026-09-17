from core.core import optimizer

def test():
    result = optimizer("Could you please build a calculator")
    assert  result.optmizedPrompt == "should be: build a calculator"
