from sqlalchemy.orm import Session
import sys
from pathlib import Path
import kiya.models as models,kiya.schemas as schemas
                  

#STUDENT

def get_student(db:Session , id:int):
    return db.query(models.Student).filter(models.Student.STID == id).first()

def get_students_list(db:Session , skip:int = 0 , limit:int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(STID = student.STID , FName = student.FName , LName = student.LName , Father = student.Father , Birth = student.Birth , IDS = student.IDS , BornCity = student.BornCity , Address = student.Address , PostalCode = student.PostalCode , CPhone = student.CPhone , HPhone = student.HPhone , Department = student.Department , Major = student.Major , Married = student.Married , ID = student.ID)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db:Session , id : int):
    db_student = db.query(models.Student).filter(models.Student.STID == id).first()
    if db_student:
        Name= f"{db_student.FName}{db_student.LName}"
        db.delete(db_student)
        db.commit()
        return {"message" : "Student {Name} deleted"}
    return{"message" : "Student not found"}

def update_student(db: Session, id :int , student : schemas.Student):
    db_student = db.query(models.Student).filter(models.Student.STID == id).first()
    if db_student:
        db_student.FName = student.FName
        db_student.LName = student.LName
        db_student.Father = student.Father
        db_student.Birth = student.Birth
        db_student.BornCity = student.BornCity
        db_student.Address = student.Address
        db_student.PostalCode = student.PostalCode
        db_student.CPhone = student.CPhone
        db_student.HPhone = student.HPhone
        db_student.Department = student.Department
        db_student.Major = student.Major
        db_student.Married = student.Married
        db_student.IDS = student.IDS
        db_student.ID = student.ID
        db.commit()
        db.refresh(db_student)
        return {"message" : f"the student {db_student.STID} updated."}
    return {"message" : "Dars not found"}



#TEACHER

def get_teacher(db:Session , id:int):
    return db.query(models.Teacher).filter(models.Teacher.LID == id).first()

def get_teachers_list(db:Session , skip:int = 0 , limit:int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()

def create_teacher(db: Session, teacher: schemas.Teacher):
    db_teacher = models.Teacher(LID= teacher.LID , FName = teacher.FName , LName = teacher.LName , Birth = teacher.Birth , ID = teacher.ID , BornCity = teacher.BornCity , Address = teacher.Address , PostalCode = teacher.PostalCode , CPhone = teacher.CPhone , HPhone = teacher.HPhone , Department = teacher.Department , Major = teacher.Major)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db:Session , id : int):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.LID == id).first()
    if db_teacher:
        Name= f"{db_teacher.FName}{db_teacher.LName}"
        db.delete(db_teacher)
        db.commit()
        return {"message" : "Teacher {Name} deleted"}
    return {"message" : "Teacher not found"}

def update_teacher(db: Session, id :int , teacher : schemas.Teacher):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.LID == id).first()
    if db_teacher:
        db_teacher.LName = teacher.LName
        db_teacher.Birth = teacher.Birth
        db_teacher.BornCity = teacher.BornCity
        db_teacher.Address = teacher.Address
        db_teacher.PostalCode = teacher.PostalCode
        db_teacher.CPhone = teacher.CPhone
        db_teacher.HPhone = teacher.HPhone
        db_teacher.Department = teacher.Department
        db_teacher.Major = teacher.Major
        db_teacher.ID = teacher.ID
        db.commit()
        db.refresh(db_teacher)
        return {"message" : f"the teacher {db_teacher.LID} updated."}
    return {"message" : "Teacher not found"}







#DARS

def get_dars(db:Session , id:int):
    return db.query(models.Dars).filter(models.Dars.CID == id).first()

def get_dars_list(db:Session , skip:int = 0 , limit:int = 100):
    return db.query(models.Dars).offset(skip).limit(limit).all()

def create_dars(db: Session, dars: schemas.Dars):
    db_dars = models.Dars(CID= dars.CID , CName = dars.CName , Department = dars.Department , credit = dars.credit)
    db.add(db_dars)
    db.commit()
    db.refresh(db_dars)
    return db_dars

def delete_dars(db:Session , id : int):
    db_dars = db.query(models.Dars).filter(models.Dars.CID == id).first()
    if db_dars:
        Name= f"{db_dars.CName}"
        db.delete(db_dars)
        db.commit()
        return{"message" : f"Dars {Name} deleted"}
    return {"message" : "Dars not found"}

def update_dars(db: Session, id :int , dars : schemas.Dars):
    db_dars = db.query(models.Dars).filter(models.Dars.CID == id).first()
    if db_dars:
        db_dars.CName = dars.CName
        db_dars.Department= dars.Department
        db_dars.credit = dars.credit
        db.commit()
        db.refresh(db_dars)
        return {"message" : f"the dars {db_dars.CID} updated."}
    return {"message" : "Dars not found"}
