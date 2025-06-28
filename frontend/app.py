# import streamlit as st
# import requests

# st.title("📅 AI Appointment Scheduler")
# # backend_url="https://calendar-agent-z257.onrender.com/chat"
# backend_url = "https://calendar-agent-1y6h.onrender.com/chat" 
# user_input = st.chat_input("Type your message to book an appointment...")

# if user_input:
#     response = requests.post("http://localhost:8000/chat", json={"text": user_input})
#     # Replace local backend with deployed backend
#     # response = requests.post(backend_url, json={"text": user_input})


#     reply = response.json().get("reply", "No reply.")
#     st.write(f"🤖 {reply}")

import streamlit as st
import requests

st.title("📅 AI Appointment Scheduler")

# Replace with your deployed FastAPI URL
backend_url = "https://your-fastapi-backend.onrender.com/chat"

user_input = st.chat_input("Type your message to book an appointment...")

if user_input:
    with st.spinner("Talking to the calendar agent..."):
        try:
            response = requests.post(backend_url, json={"text": user_input})
            reply = response.json().get("reply", "No reply.")
        except Exception as e:
            reply = f"⚠️ Error: {e}"
        st.write(f"🤖 {reply}")




# st.title("📅 AI Appointment Scheduler")

# backend_url = "https://calendar-agent-1y6h.onrender.com/chat"  # Your deployed backend URL

# user_input = st.chat_input("Type your message to book an appointment...")

# if user_input:
#     try:
#         response = requests.post(backend_url, json={"text": user_input})
#         response.raise_for_status()
#         reply = response.json().get("reply", "No reply from backend.")
#     except Exception as e:
#         reply = f"Error contacting backend: {e}"
#     st.write(f"🤖 {reply}")
# import streamlit as st
# import requests

# st.title("📅 AI Appointment Scheduler")

# # ✅ Deployed backend URL (from Render)
# backend_url = "https://calendar-agent-1.onrender.com/chat"


# user_input = st.chat_input("Type your message to book an appointment...")

# if user_input:
#     try:
#         response = requests.post(backend_url, json={"text": user_input})
#         response.raise_for_status()
#         reply = response.json().get("reply", "No reply from backend.")
#     except Exception as e:
#         reply = f"❌ Error contacting backend: {e}"
#     st.write(f"🤖 {reply}")
