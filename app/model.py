from sqlalchemy import Column, Integer, String, Float, text, TIMESTAMP, ForeignKey
from config import Base
from sqlalchemy.orm import relationship

class UserProfile(Base):
    __tablename__ = 't_user_profile'

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    created_by = Column(String, server_default='nurtura_api')
    updated_date = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_by = Column(String, server_default='nurtura_api')
    user_credential = relationship("UserCredential", back_populates="user_profile", uselist=False)

class UserCredential(Base):
    __tablename__ = 't_user_credential'

    user_id = Column(Integer, ForeignKey('t_user_profile.user_id', ondelete='CASCADE'), primary_key=True)
    hashed_password = Column(String)
    user_profile = relationship("UserProfile", back_populates="user_credential")
