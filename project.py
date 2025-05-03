#The file will handle user input, selecting business components, identify technical uncertainties, and memo search functionality

from sqlalchemy.orm import Session
from models import BusinessComponent, TechnicalUncertainty, Memo

#Function to add business components
def add_business_component(db:Session, user_id: int, name: str, description: str):
    new_component=BusinessComponent(name=name, description=description, user_id=user_id)
    db.add(new_component)
    db.commit()
    db.refresh(new_component)
    return new_component

#Function to add Technical Uncertainty
def add_technical_uncertainty(db:Session, user_id: int, name: str, description: str):
    new_uncertainty=TechnicalUncertainty(name=name, description=description, user_id=user_id)
    db.add(new_uncertainty)
    db.commit()
    db.refresh(new_uncertainty)
    return new_uncertainty

#Function to search and filter memos
def search_memos(db:Session, user_id: int, search_term: str):
    return db.query(Memo).filter(Memo.user_id==user_id,Memo.title.like(f"%{search_term}%")).all()

#Function to update technical uncertainty selection

def update_technical_uncertainty_selection(db:Session, uncertainty_id: int, is_selected: int):
    uncertainty=db.query(TechnicalUncertainty).filter(TechnicalUncertainty.uncertainty_id==uncertainty_id).first()
    uncertainty.is_selected=is_selected
    db.commit()
    db.refresh(uncertainty)
    return uncertainty



