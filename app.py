import streamlit as st
import openai
import os

# Streamlit App Title
st.title("Shripanditji - Your Virtual Assistant for Poojas and Rituals")
st.caption("💬 A spiritual chatbot powered by OpenAI")

# Fetch the OpenAI API key from Streamlit Secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize conversation state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Namaste! How can I assist you with your pooja or mantra guidance today?"}
    ]

# Display chat messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input for user prompt
if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state["messages"]
        )
        msg = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown(
    "---\n**Note:** If your requested pooja guide or mantra explanation is unavailable, please consult your local priest for assistance."
)
