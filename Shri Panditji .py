import streamlit as st

def get_pooja_guide(pooja_name, language):
    # Placeholder function to return pooja details. Replace with actual data.
    pooja_guides = {
        "Satyanarayan Pooja": {
            "English": "Step-by-step guide for Satyanarayan Pooja in English...",
            "Hindi": "सत्यनारायण पूजा के लिए चरण-दर-चरण मार्गदर्शिका हिंदी में..."
        },
        "Lakshmi Pooja": {
            "English": "Step-by-step guide for Lakshmi Pooja in English...",
            "Hindi": "लक्ष्मी पूजा के लिए चरण-दर-चरण मार्गदर्शिका हिंदी में..."
        }
    }
    return pooja_guides.get(pooja_name, {}).get(language, "Sorry, this pooja guide is not available in the selected language.")

# Streamlit App
st.title("Virtual Pooja Assistant")
st.markdown(
    """Welcome to the **Virtual Pooja Assistant**. This tool will guide you step-by-step to perform Hindu poojas at home with devotion and accuracy.""")

# User Input
pooja_name = st.text_input("Please specify the name of the pooja you wish to perform:")
language = st.selectbox("Please specify your preferred language:", ["English", "Hindi"])

# Fetch and Display Pooja Guide
if st.button("Get Pooja Guide"):
    if pooja_name and language:
        guide = get_pooja_guide(pooja_name, language)
        st.markdown("### Pooja Guide")
        st.write(guide)
    else:
        st.error("Please provide both the name of the pooja and your preferred language.")

st.markdown(
    "---\n**Note:** If your requested pooja guide is unavailable, please consult your local priest for assistance."
)
