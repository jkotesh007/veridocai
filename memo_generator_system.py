import streamlit as st
import os
from dotenv import load_dotenv
from utils.session_state import initialize_session_state

#Load Environment Variables
load_dotenv()

#Configure the Page
st.set_page_config(
    page_title="R&D Tax Credit Documentation System",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    #Initialize Session State
    initialize_session_state()

    #Main Page header
    st.title("R&D Tax Credit Documentation System")

    st.markdown("""
    ##Welcome to the R&D Tax Credit Documentation System
    
    This application helps you generate comprehensive R&D Tax Credit documentation based on project notes and other supporting documents.
    
    ##How to use this application:
    
    1.**Upload Documents**: Start by uploading project notes, employee lists, and any other relevant documents
    2.**Verify Business Component**: Review and edit the automatically generated business component description
    3.**Review Activities & Uncertainties**:Confirm the extracted activities and select relevant technical uncertainties
    4.**Verify Information Sought**: Review and edit the information sought descriptions
    5.**Generate Final Document**: Review the complete document and export it in your preferred format
    
    Navigate through the process using sidebar menu
    
    """)

    #Display current project info if available

    if st.session_state.get('project_name'):
        st.sidebar.success(f"Current Project:{st.session_state.project_name}")

    #Quick start buttons
    st.subheader("Quick Start")
    col1,col2,col3=st.columns(3)

    with col1:
        if st.button("New Project", use_container_width=True):
            st.switch_page("pages/01_document_upload.py")

    with col2:
        if st.button("Load Example",use_container_width=True):
            st.session_state.project_name="Example Project"
            st.session_state.project_notes="Example Project Notes..."
            st.rerun()

    with col3:
        if st.button("Settings",use_container_width=True):
            st.switch_page("pages/06_settings.py")

if __name__=="__main__":
    main()

