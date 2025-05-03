from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from models import User

#Hash Password
def hash_password(password: str):
    return generate_password_hash(password)

#verify Password
def verify_password(hashed_password, plain_password):
    return check_password_hash(hashed_password, plain_password)

#Register User
def register_user(db: Session, username: str, email: str, password: str):
    hashed_password = hash_password(password)
    db_user=User(username=username, email=email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Authenticate User
def authenticate_user(db:Session, username: str, password: str):
    db_user=db.query(User).filter(User.username == username).first()
    if db_user and verify_password(db_user.password, password):
        return db_user
    return None


        
