import streamlit as st
from llama_index.llms.openai import OpenAI
import cchardet as chardet
# hi


st.title('Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(a):
    llm = OpenAI(temperature=0.7, openai_api_key = openai_api_key)
    response=llm(a)
    st.info(response)

with st.form('my_form'):
    text = st.text_area('Enter your prompt:')
    uploaded_file = st.file_uploader('Upload a file', type=['txt', 'pdf', 'docx', '.png'])
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        if uploaded_file:
             file_content = uploaded_file.read()
            for encoding in known_encodings:
                try:
                    file_content = file_content.decode(encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                st.error("Unable to decode file content with known encodings")
                return
            generate_response(text, file_content)
        else:
            generate_response(text)
