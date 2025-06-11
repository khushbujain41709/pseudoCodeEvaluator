# streamlit_app.py
import streamlit as st
from transformers import pipeline

st.title("Pseudo Code Evaluator")

problem = st.text_area("Problem Statement")
code = st.text_area("Pseudo Code")

if st.button("Evaluate"):
    pipe = pipeline("text-generation", model="pseudo_eval_model", tokenizer="pseudo_eval_model")
    prompt = f"Problem: {problem}\nCode:\n{code}\nEvaluate:"
    response = pipe(prompt, max_new_tokens=150)
    st.write("### Feedback & Marks")
    st.success(response[0]["generated_text"])