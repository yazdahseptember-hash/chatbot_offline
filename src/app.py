import utils
import streamlit as st

st.title('CHATBOT PROJECT')

if 'message' not in st.session_state:
    st.session_state['message' ] = [{'role':'ai', 'content':'how can i help you'}]

for msg in st.session_state['message']:
    st.chat_message(msg['role']).write(msg['content'])

prompt = st.chat_input()
model = 'qwen2.5-coder:7b'

if prompt:
    st.chat_message('user').write(prompt)
    st.session_state['message'].append({
        'role': 'user',
        'content': prompt
    })

    with st.spinner('generation response ...'):
        respons = utils.call_ollama_model(model, prompt)

    st.chat_message('ai').write(respons)
    st.session_state['message'].append({'role':'ai' , 'content':respons})