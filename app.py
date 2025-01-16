import streamlit as st
import openai
import os

# Streamlit App Title
st.title("Shripanditji - Your Virtual Assistant for Poojas and Rituals")
st.markdown(
    """Welcome to **Shripanditji**, your one-stop assistant for performing Hindu poojas and rituals at home with devotion and accuracy. Choose a tool below to get started."""
)

# Fetch the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Error: OpenAI API key not found. Please set it as an environment variable.")
else:
    # Tool Selection
    tool = st.selectbox("Select a tool:", ["Pooja Guide Generator", "Mantra Explanation Generator"])

    if tool == "Pooja Guide Generator":
        st.header("Pooja Guide Generator")
        # User Input: Pooja Name
        pooja_name = st.text_input("Enter the name of the pooja you wish to perform:")
        # User Input: Preferred Language
        language = st.selectbox("Select your preferred language:", ["English", "Hindi"])

        if st.button("Generate Pooja Guide"):
            if pooja_name.strip():
                def generate_pooja_guide(api_key, pooja_name, language):
                    """
                    Generates a detailed guide for the specified pooja in the chosen language.

                    Parameters:
                        api_key (str): OpenAI API key.
                        pooja_name (str): The name of the pooja.
                        language (str): The preferred language for the guide.

                    Returns:
                        str: A detailed pooja guide or an error message.
                    """
                    openai.api_key = api_key

                    prompt = (
                        f"You are a Virtual Pooja Assistant designed to provide step-by-step guidance for performing {pooja_name} in {language}. "
                        "Your response should include all relevant details, such as mantras, aartis, shlokas, and systematic instructions for preparation, execution, and conclusion. "
                        "Ensure cultural and linguistic authenticity while maintaining a serene and devotional tone. Encourage environmentally friendly and safe practices."
                    )

                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are an expert at generating detailed pooja guides."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=1000
                        )
                        return response.choices[0].message.content.strip()
                    except openai.error.OpenAIError as e:
                        return f"Error generating pooja guide: {str(e)}"

                guide = generate_pooja_guide(api_key, pooja_name, language)
                if guide:
                    st.markdown("### Pooja Guide")
                    st.write(guide)
                else:
                    st.error("Could not generate the pooja guide. Please try again.")
            else:
                st.error("Pooja name cannot be empty. Please enter a valid name.")

    elif tool == "Mantra Explanation Generator":
        st.header("Mantra Explanation Generator")
        # User Input: Mantra
        mantra = st.text_area("Enter the mantra for which you want an explanation:")
        # User Input: Preferred Language
        language = st.selectbox("Select your preferred language for explanation:", ["English", "Hindi"])

        if st.button("Generate Explanation"):
            if mantra.strip():
                def generate_mantra_explanation(api_key, mantra, language):
                    """
                    Generates an explanation for the given mantra in the chosen language.

                    Parameters:
                        api_key (str): OpenAI API key.
                        mantra (str): The mantra to explain.
                        language (str): The preferred language for the explanation.

                    Returns:
                        str: An explanation of the mantra or an error message.
                    """
                    openai.api_key = api_key

                    prompt = (
                        f"You are a spiritual assistant with expertise in Hindu mantras. Provide a detailed explanation of the mantra '{mantra}' in {language}. "
                        "Explain its meaning, significance, and context in a clear and devotional tone."
                    )

                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are an expert at explaining Hindu mantras."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=1000
                        )
                        return response.choices[0].message.content.strip()
                    except openai.error.OpenAIError as e:
                        return f"Error generating mantra explanation: {str(e)}"

                explanation = generate_mantra_explanation(api_key, mantra, language)
                if explanation:
                    st.markdown("### Mantra Explanation")
                    st.write(explanation)
                else:
                    st.error("Could not generate the mantra explanation. Please try again.")
            else:
                st.error("Mantra cannot be empty. Please enter a valid mantra.")

st.markdown(
    "---\n**Note:** If your requested pooja guide or mantra explanation is unavailable, please consult your local priest for assistance."
)
