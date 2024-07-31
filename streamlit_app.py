import streamlit as st
import requests

# FastAPI endpoint
FASTAPI_URL = "http://127.0.0.1:8000/process"

# Function to send user input to FastAPI and get response
def get_response_from_backend(prompt):
    response = requests.post(FASTAPI_URL, json={"prompt": prompt})
    return response.json().get("response", "Error: No response from backend")
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with backend: {e}")
        return "Error: Could not connect to the backend."

# Title of the app
st.title("Your Beekeeping assistant")

# Container to display chat messages
chat_container = st.container()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing messages in the chat
with chat_container:
    for message in st.session_state.messages:
        st.write(message)

# Text input for user message
user_input = st.text_input("Type your message here:")

# Send button
if st.button("Send"):
    if user_input:
        response = get_response_from_backend(user_input)
        st.session_state.messages.append(f"You: {user_input}")
        st.session_state.messages.append(f"Bot: {response}")
        st.experimental_rerun()  # Rerun the app to update the chat display

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
