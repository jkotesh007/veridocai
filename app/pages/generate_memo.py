import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from app.utils import file_handler,ai_handler
def generate_memo():
    st.title("Generate IRS Project Memo")
    notes_files=file_handler.list_saved_notes()
    if not notes_files:
        st.warning("No project notes found. Please upload project notes first")
        return
    selected_file=st.selectbox("Select Project Notes",notes_files)
    if st.button("Generate Memo"):
        notes_content=file_handler.read_project_notes(selected_file)

        if not notes_content:
            st.error("Failed to read the selected project notes"),
            return

        with st.spinner('Generating Memo.. This may take a few seconds...'):
            generated_memo=ai_handler.generate_memo_from_notes(notes_content)
        if generated_memo:
            st.success("Memo generated successfully")
            #Diisplay generated Memo
            st.subheader("Generated Memo")
            st.text_area("IRS Project Memo",value=generated_memo,height=500)

            #Option to download
            file_handler.save_generated_memo(generated_memo)

            st.download_button(
                label="Download Memo as Text File",
                data=generated_memo,
                file_name="generated_memo.txt",
                mime="text/plain"
            )
        else:
            st.error("Failed to generate memo")
if __name__=="__main__":
    generate_memo()
