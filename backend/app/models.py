from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer, primary_key=True, index=True)
    distance = Column(Float, nullable=False)
    pace = Column(String, nullable=False)
    rpe = Column(Integer, default=5)
    notes = Column(String, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
