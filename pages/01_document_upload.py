import streamlit as st
import pandas as pd
import os
from utils.session_state import initialize_session_state
from utils.pdf_utils import extract_text_from_pdf
from models.document_processor import process_project_notes

#Initialize session state
initialize_session_state()
st.title("Document Upload")
st.markdown("Upload your project documents to begin the R&D tax credit documentation process.")

#Project name input
project_name=st.text_input("Project Name", value=st.session_state.get('project_name',''))

#Project notes input

st.subheader("Project Notes")
notes_tab,file_tab=st.tabs(["Enter Text","Upload File"])

with notes_tab:
    project_notes=st.text_area(
        "Enter project notes",
        value=st.session_state.get('project_notes',''),
        height=300,
        help="Paste your project notes here. Include as much detail as possible about the project activities."
    )

with file_tab:
    notes_file=st.file_uploader("Upload project notes", type=["txt","pdf"])
    if notes_file:
        if notes_file.type=="application/pdf":
            project_notes=extract_text_from_pdf(notes_file)
        else:
            project_notes=notes_file.getvalue().decode("utf-8")
        st.success(f"Successfully extracted text from {notes_file.name}")

#Employee data upload
st.subheader("Employee Information (Optional)")
employee_file=st.file_uploader("Upload employee list",type=["xlsx","csv"])
employee_data=None

if employee_file:
    try:
        if employee_file.name.endswith('.csv'):
            employee_data=pd.read_csv(employee_file)
        else:
            employee_data=pd.read_excel(employee_file)

        st.success(f"Successfully loaded employee data from {employee_file.name}")
        st.dataframe(employee_data.head())
    except Exception as e:
        st.error(f"Error loading employee data: {str(e)}")

#Additional Documents
st.subheader("Additional documents")
additional_file=st.file_uploader("Upload additional documents", type=["pdf"],accept_multiple_files=True)
additional_documents={}

if additional_file:
    for file in additional_file:
        try:
            text=extract_text_from_pdf(file)
            additional_documents[file.name]=text
            st.success(f"successfully extracted text from {file.name}")
        except Exception as e:
            st.error(f"Error processing file {file.name}: {str(e)}")

#Process Button
if st.button("Process Documents"):
    if not project_name:
        st.error("Please enter a project name")
    elif not project_notes:
        st.error("Please enter project notes or upload a file.")
    else:
        with st.spinner("Processing Documents..."):
            #Save to session state
            st.session_state.project_name=project_name
            st.session_state.project_notes=project_notes
            st.session_state.employee_data=employee_data
            st.session_state.additional_documents=additional_documents

            #Process the Documents
            processed_data=process_project_notes(project_notes,employee_data,additional_documents,model=st.session_state.openai_model,temperature=st.session_state.temperature)

            #Store processed data in session state
            st.session_state.entities=processed_data.get("entities")


            #Update workflow state
            st.session_state.current_step=2

            #Navigate to the next step
            st.success("Documents Processed Successfully")
            st.rerun()
            st.switch_page("pages/02_business_component.py")













