import openai
import streamlit as st
import re

def summarize(prompt):
    augmented_prompt = f"Generate a title or headline about the following text: {prompt}"
    try:
        st.session_state["summary"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=500,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
