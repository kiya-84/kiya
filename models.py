from sqlalchemy import  Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from kiya.database import Base
import sys
from pathlib import Path

#STUDENT

class Student(Base):  
    __tablename__ = "students"
    STID = Column(String,primary_key=True, unique=True, index=True)
    FName = Column(String)
    LName = Column(String)
    Father = Column(String)
    Birth = Column(String)
    IDS = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CPhone = Column(Integer)
    HPhone = Column(Integer)
    Department = Column(String)
    Major = Column(String)
    Married = Column(String)
    ID = Column(String)
  
 

#TEACHER   

class Teacher(Base):
    __tablename__ = "teachers"  
    LID = Column(String,primary_key=True, unique=True, index=True)
    FName = Column(String)
    LName = Column(String)
    Birth = Column(String)
    ID= Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(Integer)
    CPhone = Column(Integer)
    HPhone = Column(Integer)
    Department = Column(String)
    Major = Column(String)


#DARS

class Dars(Base):
    __tablename__ = "dars"
    CID = Column(String,primary_key=True, unique=True, index=True)
    CName = Column(String)
    Department = Column(String)
    credit = Column(Integer)



