import streamlit as st
from llama_index.llms.openai import OpenAI
import chardet


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
            # Read the content of the uploaded file
            file_content = uploaded_file.read()
            result = chardet.detect(file_content)
            encoding = result['encoding']
            file_content = file_content.decode(encoding)
            generate_response(text, file_content)
        else:
            generate_response(text) 
