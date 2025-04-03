import openai
import os

# Fetch OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OpenAI API key not found. Please set it as an environment variable named 'OPENAI_API_KEY'.")

# Set the API key
openai.api_key = api_key

# Define the system prompt for the custom GPT
LEARN_KANNADA_PROMPT = """
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

def get_kannada_response(user_query: str, model: str = "gpt-3.5-turbo") -> str:
    """
    Sends a query to the Learn Kannada GPT and returns a structured response.

    Args:
        user_query (str): The user's question or phrase to learn in Kannada.
        model (str): The OpenAI model to use. Default is 'gpt-3.5-turbo'.

    Returns:
        str: The GPT response containing Kannada translation, transliteration, explanation, and example sentence.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": LEARN_KANNADA_PROMPT.strip()},
                {"role": "user", "content": user_query.strip()}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    except openai.error.OpenAIError as e:
        return f"❌ Error from OpenAI: {str(e)}"

# Optional: CLI usage for testing or local use
if __name__ == "__main__":
    print("🗣️ Learn Kannada - CLI Assistant")
    print("Type your query below (e.g., How do I say 'Good night' in Kannada?)")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input(">> ")
        if user_input.lower().strip() == "exit":
            print("👋 Goodbye! Keep learning Kannada!")
            break
        elif not user_input.strip():
            print("⚠️ Please enter a valid question.")
            continue
        reply = get_kannada_response(user_input)
        print("\n" + reply + "\n" + "-"*50 + "\n")
