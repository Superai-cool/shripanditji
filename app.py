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

# Dropdown for Pooja Name
pooja_list = [
    "Satyanarayan Pooja", "Lakshmi Pooja", "Ganesh Chaturthi Pooja", "Durga Pooja", "Hanuman Pooja",
    "Shivratri Pooja", "Navratri Pooja", "Diwali Pooja", "Kalash Sthapana", "Chhath Pooja",
    "Kuber Pooja", "Vishnu Pooja", "Gayatri Pooja", "Rudra Abhishek", "Saraswati Pooja",
    "Ram Navami Pooja", "Tulsi Vivah", "Makar Sankranti Pooja", "Pitru Tarpan", "Bhoomi Poojan"
]
pooja_name = st.selectbox("Select a Pooja Name:", options=pooja_list + ["Custom"])
if pooja_name == "Custom":
    pooja_name = st.text_input("Enter the Pooja Name:")

# Dropdown for Language
language_list = ["Hindi", "English", "Marathi", "Tamil", "Gujarati"]
language = st.selectbox("Select a Language:", options=language_list + ["Custom"])
if language == "Custom":
    language = st.text_input("Enter the Language:")

# Generate guide if both inputs are provided
if st.button("Generate Pooja Guide"):
    if pooja_name.strip() and language.strip():
        openai.api_key = openai_api_key

        # Prepare prompt for OpenAI
        prompt = (
            f"You are a Virtual Pooja Assistant. Provide a step-by-step guide for performing {pooja_name} in {language}. "
            "Include details such as mantras, aartis, shlokas, and systematic instructions for preparation, execution, and conclusion. "
            "Ensure cultural authenticity and a devotional tone while promoting environmentally friendly practices."
        )

        # Append user input to conversation history
        st.session_state["messages"].append({"role": "user", "content": f"Pooja: {pooja_name}, Language: {language}"})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert Virtual Pooja Assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            msg = response.choices[0].message.content
            st.session_state["messages"].append({"role": "assistant", "content": msg})
            st.markdown(f"### Pooja Guide for {pooja_name} in {language}")
            st.write(msg)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please provide both a Pooja Name and a Language.")

# Display chat messages
st.markdown("---")
st.markdown("### Chat History")
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Shripanditji:** {msg['content']}")

st.markdown(
    "---\n**Note:** If your requested pooja guide or mantra explanation is unavailable, please consult your local priest for assistance."
)
