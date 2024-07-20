import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader
from langchain.llms import GooglePalm
from langchain_google_genai import GoogleGenerativeAI

api_key = st.secrets["api_key"] 

st.header("ResumeMatcher") 
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key, temperature=0.1)

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
job=st.text_area("add job description")
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    
    
    resume=text

    prompt=f"""check strictly whether the {job} matches with the following details {resume}
    if it does not matches just say no and then  suggest some skills needed to learn """
    if (len(text)==0):
        st.write("upload a valid file")
    else:
        st.write(llm.invoke(prompt))
    

