# Veloce

Veloce is a Python-based prompt optimization tool designed to reduce unnecessary token usage in LLM prompts while preserving the original instruction.

It uses rule-based prompt compression to remove redundant language and replace verbose phrases with shorter alternatives. Veloce also provides token usage statistics, a command-line interface, benchmarking tools, and a REST API built with FastAPI.

## Features

- Rule-based prompt optimization
- Removal of unnecessary or redundant phrases
- Compression of verbose phrases into shorter alternatives
- Token counting using `tiktoken`
- Before-and-after token usage statistics
- Percentage token reduction calculation
- Command-line interface
- REST API built with FastAPI
- Request validation using Pydantic
- Automated testing with pytest
- Benchmarking across multiple prompts

## Example

### Input

```text
Could you please build a calculator
```

### Optimized Output

```text
build a calculator
```

Veloce also calculates statistics such as:

```text
Original tokens: 6
Optimized tokens: 3
Tokens saved: 3
Reduction: 50%
```

Token counts may vary depending on the tokenizer and input.

## How It Works

Veloce processes a prompt through several stages:

```text
User Prompt
    |
    v
Optimization Rules
    |
    v
Prompt Cleanup
    |
    v
Token Analysis
    |
    v
Optimized Prompt + Statistics
```

Optimization rules are separated from the core application logic so that new transformations can be added without modifying the main optimizer.

For example:

```text
"please"       -> ""
"could you"    -> ""
"in order to"  -> "to"
```

The optimizer then compares the token count of the original and optimized prompts.

## Tech Stack

- Python
- FastAPI
- Pydantic
- tiktoken
- pytest
- Uvicorn

## Project Structure

```text
Veloce/
├── benchmarks/
│   ├── benchmarks.py
│   └── prompts.json
├── core/
│   ├── __init__.py
│   ├── core.py
│   ├── rules.py
│   └── tokenCounter.py
├── tests/
│   └── test_veloce.py
├── api.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd Veloce
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Command-Line Usage

Veloce can optimize prompts directly from the command line.

```bash
python app.py "Could you please build me a calculator"
```

Example output:

```text
build me a calculator
```

Run:

```bash
python app.py --help
```

to view the available CLI options.

## REST API

Veloce includes a REST API built with FastAPI.

Start the development server:

```bash
uvicorn api:app --reload
```

Once the server is running, FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### Optimize a Prompt

**Endpoint**

```text
POST /optimize
```

Example request:

```json
{
  "prompt": "Could you please build me a calculator"
}
```

Example response:

```json
{
  "optimized_prompt": "build me a calculator",
  "original_tokens": 6,
  "optimized_tokens": 4,
  "tokens_saved": 2,
  "reduction_percentage": 33.33
}
```

## Benchmarking

Veloce includes a benchmarking system for evaluating token reduction across multiple prompts.

The benchmark tracks:

- Number of prompts tested
- Total original tokens
- Total optimized tokens
- Total tokens saved
- Overall token reduction percentage

Run the benchmark with:

```bash
python benchmarks/benchmarks.py
```

Early development benchmarks demonstrated measurable token reduction, but larger and more diverse datasets are needed before drawing conclusions about general optimization performance.

## Testing

Veloce uses pytest for automated testing.

Run the test suite with:

```bash
python -m pytest
```

Tests are used to verify optimization behavior and identify transformations that could unintentionally change the meaning of a prompt.

## Current Limitations

Veloce currently relies primarily on deterministic rule-based optimization.

This approach is fast and predictable, but it cannot always determine whether a phrase is unnecessary based on context. For example, removing words from quoted text or requested output could change the user's intended result.

Future versions will focus on improving semantic preservation while achieving greater token reduction.

## Roadmap

Planned improvements include:

- Expand the optimization rule set
- Improve punctuation and whitespace handling
- Protect quoted text and code from unwanted modification
- Expand automated test coverage
- Build a larger and more diverse benchmark dataset
- Add configurable optimization levels
- Investigate context-aware and semantic compression
- Evaluate optimization quality in addition to token reduction
- Explore integration with AI coding agents

## Goal

The goal of Veloce is not simply to remove words.

The project aims to investigate how LLM prompts can be represented more efficiently while maintaining the instructions and context necessary for a model to produce the intended result.

In other words:

> **Reduce tokens without reducing intent.**
