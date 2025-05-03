#models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__='users'
    user_id=Column(Integer, primary_key=True, index=True)
    username=Column(String, unique=True,index=True)
    email=Column(String, unique=True,index=True)
    password=Column(String)

    #Relationship with Memo
    memos=relationship("Memo", back_populates="user")

class Memo(Base):
    __tablename__='memos'

    memo_id=Column(Integer, primary_key=True, index=True)
    title=Column(String, index=True)
    content=Column(Text)
    user_id=Column(Integer, ForeignKey('users.user_id'))

    #Relationship with User
    user=relationship("User",back_populates="memos")

class BusinessComponent(Base):
    __tablename__="business_components"
    component_id=Column(Integer, primary_key=True, index=True)
    name=Column(String,index=True)
    description=Column(Text)
    user_id=Column(Integer, ForeignKey('users.user_id'))

    #Relationship with User
    user=relationship("User",back_populates="business_components")

class TechnicalUncertainty(Base):
    __tablename__='technical_uncertainties'

    uncertainty_id=Column(Integer, primary_key=True, index=True)
    name=Column(String, index=True)
    description=Column(Text)
    is_selected=Column(Integer, default=0) #0=not selected, 1=Selected
    user_id=Column(Integer, ForeignKey('users.user_id'))

    #Relationship with the User
    user=relationship("User",back_populates="technical_uncertainties")

User.business_components=relationship("BusinessComponent",back_populates="user")
User.technical_uncertainties=relationship("TechnicalUncertainty",back_populates="user")
