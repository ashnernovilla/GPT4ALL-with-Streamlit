# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:22:19 2024

@author: ASHNER_NOVILLA
"""

# import streamlit as st

# prompt = st.chat_input("Say something")
# if prompt:
#     st.chat_message("user").write(prompt)
#     st.chat_message("assistant").write(f"Echo: {prompt}")


import streamlit as st

# Define custom CSS for chat layout
st.markdown(
    """
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .user-message, .assistant-message {
        display: flex;
        align-items: center;
    }
    .user-message {
        justify-content: flex-start;
    }
    .assistant-message {
        justify-content: flex-end;
        color: gray;
        font-weight: bold;
        margin-right: 10px;
    }
    .message-bubble {
        padding: 10px 15px;
        border-radius: 15px;
        max-width: 70%;
        color: white;
    }
    .user-bubble {
        background-color: #007bff;
    }
    .assistant-bubble {
        background-color: #28a745;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Placeholder for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
prompt = st.chat_input("Say something")
if prompt:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Append assistant's response
    st.session_state.messages.append({"role": "assistant", "content": f"Echo: {prompt}"})

# Render chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f'<div class="chat-container"><div class="user-message"><div class="message-bubble user-bubble">{message["content"]}</div></div></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="chat-container"><div class="assistant-message">AI BOT: <div class="message-bubble assistant-bubble">{message["content"]}</div></div></div>',
            unsafe_allow_html=True
        )
