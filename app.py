import streamlit as st
import openai
import os
from streamlit_chat import message

# Streamlit App Title
st.title("Shripanditji - Your Virtual Assistant for Poojas and Rituals")
st.markdown(
    """Welcome to **Shripanditji**, your one-stop assistant for performing Hindu poojas and rituals at home with devotion and accuracy. Interact below to get personalized guidance!"""
)

# Fetch the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Error: OpenAI API key not found. Please set it as an environment variable.")
    st.stop()
else:
    # Initialize session state for chatbot conversation
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are Shripanditji, a spiritual assistant providing guidance for Hindu poojas and mantras."}
        ]

    # Display existing messages
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"user_{i}")
        else:
            message(msg["content"], key=f"bot_{i}")

    # User input for chatbot
    with st.form("chat_input", clear_on_submit=True):
        user_input = st.text_area("Type your question or request (e.g., 'Generate a guide for Lakshmi Pooja in Hindi'):")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        # Add user message to session
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Function to get response from OpenAI
        def get_openai_response(messages):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=messages,
                    max_tokens=1000
                )
                return response.choices[0].message.content.strip()
            except openai.error.OpenAIError as e:
                return f"Error: {str(e)}"

        # Get the response and add it to the chat
        bot_response = get_openai_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

        # Display bot response
        message(bot_response, key=f"bot_{len(st.session_state.messages) - 1}")

st.markdown(
    "---\n**Note:** If your requested pooja guide or mantra explanation is unavailable, please consult your local priest for assistance."
)
