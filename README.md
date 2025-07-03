# PseudoCode Evaluator

A fine-tuned AI model that evaluates pseudo-code submissions, providing **scores** and **constructive feedback** — built with `Phi-2` + `LoRA`.

---

## Features

- **Automated Grading**: Rates pseudo-code based on correctness, readability, and handling of edge cases (e.g., 8/10).
- **Feedback Generation**: Offers suggestions for improvement (e.g., empty input handling, logic refinement).
- **Low-Cost Fine-Tuning**: Powered by **4-bit quantization** and **LoRA** for memory-efficient training.
- **Interactive Web Demo**: Test pseudo-code via a simple `Streamlit` interface.

---

## Tech Stack

- **Model**: [`microsoft/phi-2`](https://huggingface.co/microsoft/phi-2) (2.7B parameters)
- **Fine-Tuning**: LoRA (Low-Rank Adaptation)
- **Quantization**: 4-bit with `bitsandbytes`
- **Core Libraries**:
  - `transformers`
  - `peft`
  - `datasets`
  - `bitsandbytes`
- **Inference**: Hugging Face `pipeline`
- **Frontend UI**: Streamlit

---

## Installation

```bash
git clone https://github.com/your_username/pseudoCodeEvaluator.git
cd pseudoCodeEvaluator
pip install -r requirements.txt

```
---

## Usage

- **Load the Model**:
```bash
from transformers import pipeline
eval_pipe = pipeline("text-generation", model="./pseudo_eval_model")

```
- **Evaluate Pseudo-Code**:
```bash
prompt = """
Problem: Check if a string is a palindrome.
Pseudo Code: 
read str
rev = reverse(str)
if rev == str: print 'Palindrome'
"""
feedback = eval_pipe(prompt, max_new_tokens=150)[0]["generated_text"]
print(feedback)

```

---
