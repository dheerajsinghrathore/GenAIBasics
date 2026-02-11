import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import json
import os
import time
from datetime import datetime

CHAT_DIR = "chats"
os.makedirs(CHAT_DIR, exist_ok=True)


def get_open_ai_client():
    load_dotenv()
    return OpenAI()


client = get_open_ai_client()


def new_chat():
    chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(CHAT_DIR, f"{chat_id}.json")
    data = {
        "title": "New Chat",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are PyMentor, a helpful Python Tutor."
                    "Answer only Python related questions."
                    "Politley refuse non Python Questions."
                ),
            }
        ],
    }
    save_chat(file_path, data)
    return chat_id


def save_chat(path, messages):
    with open(path, "w") as f:
        json.dump(messages, f, indent=4)


def generate_chat_title(user_message):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "Generate a short title ( max 5 words)"
                "based on user message."
                "Do not use quotes",
            },
            {"role": "user", "content": user_message},
        ],
    )
    return response.output_text.strip()


def load_chat(path):
    with open(path, "r") as f:
        return json.load(f)


def list_chats():
    return sorted(os.listdir(CHAT_DIR), reverse=True)


def stream_chat_with_ai(messages, placeholder, temperature, model):
    stream = client.responses.create(
        model=model, input=messages, temperature=temperature, stream=True
    )

    full_response = ""
    for event in stream:
        if event.type == "response.output_text.delta":
            token = event.delta
            full_response += token
            placeholder.markdown(full_response)
    return full_response


st.set_page_config(page_title="pymentor", layout="centered")
st.title("🐍 PyMentor-Python Tutor ChatBot")
st.write("💡 Welcome To Your AI Powered Python Assistant")
st.caption(
    "🧚‍♀️Chat Titles |💬 Streaming| 🔄️ Resume Chat | 🎮 Controls Enabled | 🤹Multiple Chats"
)

st.sidebar.header("⚙️ Chat Settings")

if "current_chat" not in st.session_state:
    st.session_state.current_chat = new_chat()

chat_files = list_chats()
chat_titles = {}
for f in chat_files:
    try:
        data = load_chat(os.path.join(CHAT_DIR, f))
        if isinstance(data, dict) and "title" in data:
            chat_titles[f] = data["title"]
        else:
            chat_titles[f] = "Legacy Chat"
    except Exception:
        chat_titles[f] = "Corrupted Chat"

selected_chat = st.sidebar.selectbox(
    "Select Chat",
    chat_files,
    index=chat_files.index(f"{st.session_state.current_chat}.json"),
    format_func=lambda f: chat_titles[f],
)

if selected_chat.replace(".json", "") != st.session_state.current_chat:
    st.session_state.current_chat = selected_chat.replace(".json", "")
    st.rerun()

if st.sidebar.button("➕ New Chat"):
    st.session_state.current_chat = new_chat()
    st.rerun()

model = st.sidebar.selectbox("Choose Model", ["gpt-5.1", "gpt-4.1-mini"])
temperature = st.sidebar.slider(
    "Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1
)

chat_path = os.path.join(CHAT_DIR, f"{st.session_state.current_chat}.json")

chat_data = load_chat(chat_path)
messages = chat_data["messages"]

message_count = len([m for m in messages if m["role"] != "system"])
st.sidebar.metric("💬 Messages", message_count)

for msg in messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).markdown(msg["content"])

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area(
        "Ask a Python Question",
        height=100,
        placeholder="For eg: Explain Python List with examples",
    )
    submit = st.form_submit_button("Ask PyMentor")

if submit and user_input.strip():
    st.chat_message("user").markdown(user_input)
    messages.append({"role": "user", "content": user_input})

    if chat_data["title"] == "New Chat":
        chat_data["title"] = generate_chat_title(user_input)

    with st.chat_message("assistant"):
        typing = st.empty()
        typing.markdown("⌛ PyMentor Is Typing...")
        time.sleep(0.5)
        placeholder = st.empty()
        ai_reply = stream_chat_with_ai(
            messages, placeholder, model=model, temperature=temperature
        )
        typing.write("")
    messages.append({"role": "assistant", "content": ai_reply})
    save_chat(chat_path, chat_data)
    st.rerun()

if st.sidebar.button("🗑️ Delete Chat"):
    os.remove(chat_path)
    st.session_state.current_chat = new_chat()
    st.rerun()
