
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.utils import file_handler
def upload_project_notes():
    st.title("Upload Project Notes")
    st.write("Enter your project Notes Below:")

    #Text Area for Input
    project_notes=st.text_area(
        label="Project Notes",
        placeholder="Paste or Write your project Notes here...",
        height=300
    )
    if st.button("Save Notes"):
        if project_notes.strip()=="":
            st.warning("Please enter some notes before saving")
        else:
            #Save the notes using file handler
            save_status=file_handler.save_project_notes(project_notes)
            if save_status:
                st.success("Notes saved successfully")
            else:
                st.error("Failed to Save Notes, please try again later")

if __name__=="__main__":
    upload_project_notes()
