from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Run
import os

DATABASE_URL = "sqlite:///./airun.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

def add_run(distance, pace, rpe, notes):
    session = SessionLocal()
    new_run = Run(distance=distance, pace=pace, rpe=rpe, notes=notes)
    session.add(new_run)
    session.commit()
    session.refresh(new_run)
    session.close()
    return new_run

def get_runs():
    session = SessionLocal()
    runs = session.query(Run).all()
    session.close()
    return runs
