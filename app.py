import streamlit as st
import openai

# Streamlit config
st.set_page_config(page_title="Learn Kannada", page_icon="🗣️", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .main {
            background-color: #fffaf0;
        }
        textarea, input {
            font-size: 16px !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stMarkdown h4 {
            color: #1a73e8;
        }
    </style>
""", unsafe_allow_html=True)

# Title & description
st.title("🗣️ Learn Kannada")
st.markdown("#### A friendly assistant to help you learn practical Kannada – step by step!")

# API Key input
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# User question input
user_query = st.text_area("💬 Type your question in any language", placeholder="E.g., How do I say 'Where is the bus stop?' in Kannada?", height=120)

# Translate button
if st.button("🔍 Get Kannada Translation"):
    if not openai_api_key:
        st.warning("⚠️ Please enter your OpenAI API key.")
    elif not user_query.strip():
        st.warning("⚠️ Please enter a question to translate.")
    else:
        openai.api_key = openai_api_key

        # Custom system prompt
        system_prompt = """
You are "Learn Kannada" – a custom GPT designed to help users learn local, conversational Kannada in a clear, friendly, and structured way.

Users can ask questions in any language, and you must respond using this consistent four-part format:

Kannada Translation – Provide the correct modern, everyday Kannada word or sentence based on the user’s query. Avoid old-style, literary, or overly formal Kannada.

Transliteration – Show the Kannada sentence using English phonetics for easy pronunciation.

Meaning/Context – Explain the meaning in simple terms, ideally using the user’s input language.

Example Sentence – Include a realistic, locally used example sentence in Kannada with transliteration and English meaning.

Your tone must be encouraging, easy to understand, and beginner-friendly. Focus only on helping users learn practical Kannada used in daily life—not classical or textbook-only Kannada.

If a user asks something unrelated to Kannada learning, gently refuse and remind them to ask only Kannada-related questions.

Always end your response with:
Powered by WROGN Men Watches | [Buy Now](https://web.lehlah.club/s/gld8o5)
"""

        # Query OpenAI
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt.strip()},
                    {"role": "user", "content": user_query.strip()}
                ],
                temperature=0.7
            )
            reply = response.choices[0].message.content

            # Show response
            st.markdown("---")
            st.markdown("### ✅ Your Kannada Lesson")
            st.markdown(reply)

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("<center><small>✨ Made with ❤️ to help you speak Kannada like a local!</small></center>", unsafe_allow_html=True)
