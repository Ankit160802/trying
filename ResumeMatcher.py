import streamlit as st
from langchain_community.document_loaders import PyPDFLoader

st.header("ResumeMatcher")


uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
st.write(uploaded_file)
if uploaded_file is not None:
    loader=PyPDFLoader(uploaded_file)
    text=loader.load()
    whole_doc=text[0].page_content
    st.write(whole_doc)

