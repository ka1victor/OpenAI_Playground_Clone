import streamlit as st
import json

# Streamlit page configuration
st.set_page_config(page_title="OpenAI API Call Generator", layout="wide")

# API Key Input
api_key = st.text_input("OpenAI API Key", type="password")

# Model Selection
model_options = ["gpt-3.5-turbo", "gpt-4", "gpt-4-32k"]  # Updated model options
chosen_model = st.selectbox("Choose the Model", options=model_options)

# Behavior Guidelines
guidelines_prompt = st.text_area("Behavior Guidelines", height=150)

# Behavior Examples
behavior_examples = []
if st.button("Add Behavior Example"):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            user_input = st.text_area("User Message", key="user")
        with col2:
            assistant_input = st.text_area("Assistant Message", key="assistant")

    if user_input and assistant_input:
        behavior_examples.append({"user": user_input, "assistant": assistant_input})

# Reminder for Environment Variable
st.markdown("## ⚠️ Don't forget to save the `OPENAI_API_KEY` as an environment variable.")
st.markdown("If you don't know how to do that, this link might help: [How to Set an Environment Variable on Windows](https://www.google.com/search?q=how+to+set+an+environment+variable+on+windows)")

# Handling User Inputs and Generating Code
if st.button("Generate API Call Code"):
    code = f"""
from openai import OpenAI
client = OpenAI()
# Assuming you already saved the OPENAI_API_KEY as an environment variable 

chosen_model = "{chosen_model}"
guidelines_prompt = """ + json.dumps(guidelines_prompt) + """
behavior_examples = """ + json.dumps(behavior_examples) + """

completion = client.chat.completions.create(
  model=chosen_model,
  messages=[
    {"role": "system", "content": guidelines_prompt},
    # Insert behavior examples here
    {"role": "user", "content": 'actual_input'}
  ]
)

print(completion.choices[0].message)
"""
    st.code(code, language='python')
