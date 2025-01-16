import streamlit as st
import openai
import os

# Streamlit App Title
st.title("Virtual Pooja Assistant")
st.markdown(
    """Welcome to the **Virtual Pooja Assistant**. This tool will guide you step-by-step to perform Hindu poojas at home with devotion and accuracy."""
)

# Fetch the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Error: OpenAI API key not found. Please set it as an environment variable.")
else:
    # User Input: Pooja Name
    pooja_name = st.text_input("Please specify the name of the pooja you wish to perform:")

    # User Input: Preferred Language
    language = st.selectbox(
        "Please specify your preferred language:",
        ("English", "Hindi")
    )

    # Generate Guide Button
    if st.button("Get Pooja Guide"):
        if pooja_name.strip() and language:
            # Function to Generate Pooja Guide
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

                    guide = response.choices[0].message.content.strip()
                    return guide

                except openai.error.AuthenticationError:
                    return "Authentication error: Please check your OpenAI API key."
                except openai.error.OpenAIError as e:
                    return f"OpenAI API error: {str(e)}"

            # Generate and Display the Guide
            guide = generate_pooja_guide(api_key, pooja_name, language)
            if "error" in guide.lower():
                st.error(guide)
            else:
                st.markdown("### Pooja Guide")
                st.write(guide)
        else:
            st.error("Please provide both the name of the pooja and your preferred language.")

st.markdown(
    "---\n**Note:** If your requested pooja guide is unavailable, please consult your local priest for assistance."
)
