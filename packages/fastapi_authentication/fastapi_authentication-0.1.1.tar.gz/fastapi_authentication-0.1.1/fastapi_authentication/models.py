from fastapi_auth.con import Base
from sqlalchemy import  Column, Integer, String,  DateTime, Boolean
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    # profile_image = Column(String)  
    email = Column(String, unique=True, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    
    

class OTPRecord(Base):
    __tablename__ = 'otp_records'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    otp = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
