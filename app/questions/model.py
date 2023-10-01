from enum import Enum
from sqlalchemy import Column, ForeignKey
from sqlalchemy import DateTime
import uuid
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.db.base_class import Base


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    options = relationship("Option", backref="questions", lazy='noload')


class Option(Base):
    __tablename__ = 'options'
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(String)
    is_correct = Column(Boolean)
