import openai
import streamlit as st

def show_messages(text):
  messages_str = [
    f"{_['role']}:{_['content']}" for_ in st.session_state["messages"][1:]
  ]
  text.text_area("Messages"，value=str("\n\n".join(messages_str))，height=400)

BASE_PROMPT=[{"role":"system","content": "You are a helpful assistant."}]

if "messages" not in st.session_state:
  st.session state["messages"] =BASE_PROMPT

st.subheader("ChatGpT @ IEG Growth Platform Data Science")

openai.api_key=st.textinput("Paste your OpenAI API Key here", value="", type="password")
prompt=st.text_input("Prompt", value="Enter your message here...")

if st.button("Send"):
  with st.spinner("Generating response..."):
    st.session_state["messages"] += [{"role": "user","content": prompt}]
    response =openai.ChatCompletion.create(
      model="gpt-3.5-turbo", messages=st.session_state["messages"]
    )
    messageresponse = response["choices"][8]["message"]["content"]
    st.session_state["messages"] +=[
      {"role":"system","content": message_response}
    ]

if st.button("Clear"):
  st.session_state["messages"] = BASE_PROMPT

text =st.empty()
show_messages(text)
