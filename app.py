import streamlit as st
import openai
import os

# App Title
st.title("🗣️ Welcome to the Learn Kannada Assistant")

# Fetch API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ Error: OpenAI API key not found. Please set it as an environment variable named 'OPENAI_API_KEY'.")
else:
    # User input: query
    user_query = st.text_area("💬 Ask your question in any language:", placeholder="E.g., How do I say 'Good morning' in Kannada?")

    # Submit button
    if st.button("🔍 Get Kannada Translation"):
        if user_query.strip():
            def get_kannada_response(api_key, user_input):
                """
                Calls OpenAI GPT to return a structured Kannada learning response.

                Parameters:
                    api_key (str): OpenAI API key
                    user_input (str): User's multilingual query

                Returns:
                    str: Structured four-part Kannada learning output
                """
                openai.api_key = api_key

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

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": system_prompt.strip()},
                            {"role": "user", "content": user_input.strip()}
                        ],
                        temperature=0.7
                    )

                    result = response.choices[0].message.content.strip()
                    return result

                except openai.error.OpenAIError as e:
                    return f"❌ Error from OpenAI: {str(e)}"

            # Generate and display output
            output = get_kannada_response(api_key, user_query)

            st.markdown("### ✅ Kannada Learning Response")
            st.markdown(output)
        else:
            st.warning("⚠️ Please enter a question.")
