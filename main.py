#This will be the main application that ties everything together
import streamlit as st
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from db import init_db, SessionLocal
from auth import register_user, authenticate_user
from ai import generate_memo, TEMPLATES
from project import add_business_component, add_technical_uncertainty, search_memos, update_technical_uncertainty_selection
from models import Memo
from models import User

#Initialize db
init_db()

#Create a session for database interaction
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Register Page
def register(db: Session):
    st.subheader("Register")
    username=st.text_input("Username")
    email=st.text_input("Email")
    password=st.text_input("Password", type="password")
    confirm_password=st.text_input("Confirm Password",type="password")

    if password==confirm_password:
        if st.button("Register"):
            user=register_user(db,username,email,password)
            st.success(f"User {user.username} created successfully.")
    else:
        st.error("Passwords do not match.")

#Login Page
def Login(db: Session):
    st.subheader("Login")
    username=st.text_input("Username")
    password=st.text_input("Password", type="password")

    if st.button("Login"):
        user=authenticate_user(db,username,password)
        if user:
            st.session_state['user_id']=user.user_id
            st.session_state['username']=user.username
            st.success(f"Welcome {user.username}")
            return True
        else:
            st.error("Invalid username or password.")
    return False

#Memo generation page
def memo_generation(db: Session):
    st.subheader("Generate Project Memo")

    # Check if user is logged in
    if 'user_id' not in st.session_state:
        st.warning("Please log in to generate memos.")
        return

    project_notes = st.text_area("Enter Project Notes")

    selected_template = st.selectbox("Select Memo Template", list(TEMPLATES.keys()))

    memo_content = ""
    if st.button("Generate Memo"):
        template = TEMPLATES[selected_template]
        memo_content = generate_memo(project_notes, template)
        st.session_state.generated_memo = memo_content  # Save to session

    if 'generated_memo' in st.session_state:
        st.write("Generated Memo")
        st.text_area("Memo", value=st.session_state.generated_memo, height=300)

        memo_title = st.text_input("Memo Title", "")

        if st.button("Save Memo"):
            if not memo_title.strip():
                st.warning("Please provide a title for the memo before saving.")
                return

            new_memo = Memo(
                title=memo_title,
                content=st.session_state.generated_memo,
                user_id=st.session_state.user_id
            )
            try:
                db.add(new_memo)
                db.commit()
                db.refresh(new_memo)
                st.success(f"Memo '{memo_title}' saved successfully!")
            except Exception as e:
                st.error(f"Error saving memo: {e}")
def main(db: Session):
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Memo Generation", "Register", "Login"])

    if page == "Memo Generation":
        memo_generation(db)
    elif page == "Register":
        register(db)
    elif page == "Login":
        Login(db)
if __name__=="__main__":
    db=SessionLocal()
    main(db)



