import streamlit as st
def initialize_session_state():
    """Initialize session state variables if they don't exist"""

    #Project Information

    if 'project_name' not in st.session_state:
        st.session_state.project_name=None

    if 'project_notes' not in st.session_state:
        st.session_state.project_notes=None

    if 'employees_data' not in st.session_state:
        st.session_state.employees_data=None

    if 'additional_documents' not in st.session_state:
        st.session_state.additional_documents=None

    #Processed Data

    if 'entities' not in st.session_state:
        st.session_state.entities=None

    if 'activities' not in st.session_state:
        st.session_state.activities=None

    if 'uncertainties' not in st.session_state:
        st.session_state.uncertainties=None

    if 'selected_uncertainties' not in st.session_state:
        st.session_state.selected_uncertainties=None

    if 'information_sought' not in st.session_state:
        st.session_state.information_sought=None

    if 'final_document' not in st.session_state:
        st.session_state.final_document=None

    #Workflow state
    if 'current_step' not in st.session_state:
        st.session_state.current_step=None

    #Settings

    if 'openai_model' not in st.session_state:
        st.session_state.openai_model='gpt-4'

    if 'temperature' not in st.session_state:
        st.session_state.temperature=0.2

    def reset_session_state():
        """Reset all session state variables except settings"""

    #Preserve settings
    model=st.session_state.openai_model
    temp=st.session_state.temperature

    #Clear everything else

    for key in list(st.session_state.keys()):
        if key not in ['openai_model', 'temperature']:
            del st.session_state[key]

    #Reinitialize
    initialize_session_state()

    #Restore Settings
    st.session_state.openai_model=model
    st.session_state.temperature=temp

