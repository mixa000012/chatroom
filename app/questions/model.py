import enum
from sqlalchemy import Column, ForeignKey
import uuid
from sqlalchemy import String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.db.base_class import Base
from app.survey.model import Survey


class QuestionTypeEnum(str, enum.Enum):
    ONE_CHOICE = 'ONE_CHOICE'
    MULTIPLE_CHOICE = 'MULTIPLE_CHOICE'
    YES_OR_NO = 'YES_OR_NO'
    FREEFORM_ANSWER = 'FREEFORM_ANSWER'


class Question(Base):
    __tablename__ = 'questions'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    survey_id = Column(UUID, ForeignKey('survey.id'))
    text = Column(String, index=True)
    type = Column(Enum(QuestionTypeEnum, name='questiontype'))
    options = relationship("Option", backref="questions", lazy='noload')


class Option(Base):
    __tablename__ = 'options'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID, ForeignKey('questions.id'))
    text = Column(String)
