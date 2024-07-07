from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import sys
from pathlib import Path

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#STUDENT

@app.get("/students/")
def read_students(skip: int = 0, limit: int = 100, db:Session= Depends(get_db)):
    students = crud.get_students(db, skip = skip , limit = limit)
    return students


@app.get("/Gstudent/{STID}/")
def read_student(STID: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, id=STID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@app.post("/CRstudent/")
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, id=student.STID)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exists")
    return crud.create_student(db=db, student=student)

@app.put("/Ustudent/{STID}/")
async def update_student(STID: int, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, id = STID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.update_student(db=db , id = STID, student = student)

@app.delete("/Dstudent/{STID}/")
def delet_student(STID: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, id=STID)
    if db_student is None:
        raise HTTPException(status_code=400, detail="Student not found")
    return crud.delete_student(db = db , id = STID)



#TEACHER

@app.get("/teacher/")
def read_teacher(skip: int = 0, limit: int = 100, db:Session= Depends(get_db)):
    teachers = crud.get_teachers(db, skip = skip , limit = limit)
    return teachers


@app.get("/Gteacher/{LIID}/")
def read_teacher(LID: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, id=LID)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher


@app.post("/CRteacher/")
def create_teacher(teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, id=teacher.LID)
    if db_teacher:
        raise HTTPException(status_code=400, detail="Teacher already exists")
    return crud.create_teacher(db=db, teacher=teacher)

@app.put("/Uteacher/{LID}/")
async def update_teacher(LID: int, teacher: schemas.Teacher, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, id = LID)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return crud.update_teacher(db=db , id = LID, teacher = teacher)

@app.delete("/Dteacher/{LID}/")
def delet_teacher(LID: int, db: Session = Depends(get_db)):
    db_teacher = crud.get_teacher(db, id=LID)
    if db_teacher is None:
        raise HTTPException(status_code=400, detail="Teacher not found")
    return crud.delete_teacher(db = db , id = LID)




#DARS


@app.get("/dars/")
def read_dars(skip: int = 0, limit: int = 100, db:Session= Depends(get_db)):
    dars = crud.get_dars(db, skip = skip , limit = limit)
    return dars


@app.get("/Gdars/{CID}/")
def read_dars(CID: int, db: Session = Depends(get_db)):
    db_dars = crud.get_dars(db, id=CID)
    if db_dars is None:
        raise HTTPException(status_code=404, detail="Dars not found")
    return db_dars


@app.post("/CRdars/")
def create_dars(dars: schemas.Dars, db: Session = Depends(get_db)):
    db_dars = crud.get_dars(db, id=dars.CID)
    if db_dars:
        raise HTTPException(status_code=400, detail="Dars already exists")
    return crud.create_dars(db=db, dars=dars)

@app.put("/Udars/{CID}/")
async def update_dars(CID: int, dars: schemas.Dars, db: Session = Depends(get_db)):
    db_dars = crud.get_dars(db, id = CID)
    if db_dars is None:
        raise HTTPException(status_code=404, detail="Dars not found")
    return crud.update_dars(db=db , id = CID, dars = dars)

@app.delete("/Ddars/{CID}/")
def delet_dars(CID: int, db: Session = Depends(get_db)):
    db_dars = crud.get_dars(db, id=CID)
    if db_dars is None:
        raise HTTPException(status_code=400, detail="Dars not found")
    return crud.delete_dars(db = db , id = CID)