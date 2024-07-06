from pydantic import BaseModel,validator, ValidationError
from fastapi import HTTPException
import re
import sys
from pathlib import Path


#STUDENT


class Student(BaseModel):
    STID : str
    FName: str
    LName : str
    Father : str
    Birth : str
    IDS : str
    BornCity : str
    Address : str
    PostalCode : str
    CPhone : str
    HPhone : str
    Department : str
    Major : str
    Married : str
    ID : str
    
    

    @validator("STID")
    def validate_stid(cls,stid):
        pattern = r"^40[0-2]114150(0[1-9]|[1-9][0-9])$"
        if not re.match(pattern , stid) or len(stid) != 11:
            raise ValueError("Invalid STID , STID must have 11 digit with the rules that we told")
        return stid

    @validator("FName")
    def validate_fname(cls,fname):
        pattern = r"^[آ-ی]{1,10}$"
        if not re.match(pattern ,fname) or len(fname) > 10:
            raise ValueError("Invalid FName , FName should have at least 10 character and should be persian")
        return fname

    @validator("LName")
    def validate_lname(cls,lname):
        pattern = r"^[آ-ی]{1,10}$"
        if not re.match(pattern ,lname) or len(lname) > 10:
            raise ValueError("Invalid LName , LName should have at least 10 character and should be persian")
        return lname

    @validator("Father")
    def validate_father(cls,father):
        pattern = r"^[آ-ی]{1,10}$"
        if not re.match(pattern ,father) or len(father) > 10:
            raise ValueError("Invalid Father name , Father name should have at least 10 character and should be persian")
        return father

    @validator("Birth")
    def validate_birth(cls,birth):
        pattern = r"^(13[0-9]{2})/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
        if not re.match(pattern ,birth):
            raise ValueError("Invalid Birth , The year part should be between 1300 to 1400, The month should be between 1 to 12 and The day part should be between 1 to 31")
        return birth

    @validator("IDS")
    def validate_ids(cls,ids):
        pattern = r"^\d{6}[آ-ی]\d{2}$"
        if not re.match(pattern ,ids) or len(ids) != 9:
            raise ValueError("Invalid IDS ,IDS should be written with the rules ")
        return ids

    @validator("BornCity")
    def validate_borncity(cls,borncity):
        pattern = r"^(ارومیه|تبریز|اردبیل|رشت|ساری|گرگان|بجنورد|مشهد|سمنان|تهران|قزوین|زنجان|سنندج|همدان|اراک|قم|بیرجند|یزد|اصفهان|خرم آباد|ایلام|کرمانشاه|کرمان|زاهدان|بندرعباس|شیراز|یاسوج|شهرکرد|اهواز|بوشهر)$"
        if not re.match(pattern ,borncity):
            raise ValueError("Invalid BornCity , BornCity should one of the capital of the content")
        return borncity
    
    @validator("Address")
    def validate_address(cls,address):
        pattern = r"^[آ-ی\s\d,.]{1,100}$"
        if not re.match(pattern ,address) or len(address) > 100:
            raise ValueError("Invalid Address , Address should be persian and have at least 100 characters")
        return address
    
    @validator("PostalCode")
    def validate_post(cls,post):
        pattern = r"^\d{10}$"
        if not re.match(pattern ,post) or len(post) != 10:
            raise ValueError("Invalid PostalCode , PostalCode should be digit and have 10 character")
        return post
    
    @validator("CPhone")
    def validate_cphone(cls,cphone):
        pattern = r"^09\d{9}$"
        if not re.match(pattern ,cphone) or len(cphone) != 11:
            raise ValueError("Invalid CPhone , CPhone should be digit and start with '09' and have 11 digit")
        return cphone
    
    @validator("HPhone")
    def validate_hphone(cls,hphone):
        pattern = r"^(021|026|025|024|023|022|028|071|072|073|074|075|076|077|078|079|081|082|083|084|085|086|087|088|089|031|032|033|034|035|036|037|038|041|042|043|044|045|046|047|051|052|053|054|055|061|062|063|064|065|066|067)\d{8}$"
        if not re.match(pattern ,hphone) or len(hphone) != 11:
            raise ValueError("Invalid HPhone , HpHone should be digit and have 11 digit and should be written with the rules")
        return hphone

    @validator("Department")
    def validate_depart(cls,depart):
        pattern = r"^(علوم اجتماعی|مدیریت|علوم پایه|فنی و مهندسی|علوم انسانی|هنر|پزشکی|حقوق|دامپزشکی)$"
        if not re.match(pattern ,depart):
            raise ValueError("Invalid Department , Department should be one of the list of departments")
        return depart

    @validator("Major")
    def validate_major(cls,major):
        pattern = r"^(مهندسی برق|مهندسی کامپیوتر|مهندسی مکانیک|مهندسی عمران|مهندسی شیمی|مهندیس صنایع|مهندسی مواد|مهندسی نقشه یرداری|مهندسی نفت|مهندسی هوافضا|مهندسی پزشکی |مهندسی راه آهن|مهندسی معدن|مهندسی کشاورزی|مهندسی نساجی|مهندسی آب|مهندسی خاک|مهندسی معماری)$"
        if not re.match(pattern ,major):
            raise ValueError("Invalid Major , Major should be one of the list of major")
        return major
    
    @validator("Married")
    def validate_married(cls,married):
        pattern = r"^(متاهل|مجرد)"
        if not re.match(pattern ,married):
            raise ValueError("Invalid Married , Married should be one of the list of married")
        return married
    
    @validator("ID")
    def validate_id(cls,id):
        pattern = r"^[1-9]\d{9}$"
        if not re.match(pattern ,id) or len(id) != 10:
            raise ValueError("Invalid ID , ID should be have 10 digit")
        return id

    


#TEACHER


class Teacher(BaseModel):
    LID : str
    FName: str
    LName : str
    Birth : str
    ID: str
    BornCity : str
    Address : str
    PostalCode : str
    CPhone : str
    HPhone : str
    Department : str
    Major : str
    LCourseIDs : str
   
    @validator("LID")
    def validate_lid(cls,lid):
        pattern = r"^\d{6}"
        if not re.match(pattern , lid) or len(lid) != 6:
            raise ValueError("Invalid LID , LID should have 6 digit")
        return lid
    
    @validator("FName")
    def validate_fname(cls,fname):
        pattern = r"^[آ-ی]{1,10}$"
        if not re.match(pattern ,fname) or len(fname) > 10:
            raise ValueError("Invalid FName , FName should have at least 10 character and should be persian")
        return fname

    @validator("LName")
    def validate_lname(cls,lname):
        pattern = r"^[آ-ی]{1,10}$"
        if not re.match(pattern ,lname) or len(lname) > 10:
            raise ValueError("Invalid LName , LName should have at least 10 character and should be persian")
        return lname
    
    @validator("Birth")
    def validate_birth(cls,birth):
        pattern = r"^(13[0-9]{2})/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
        if not re.match(pattern ,birth):
            raise ValueError("Invalid Birth , The year part should be between 1300 to 1400, The month should be between 1 to 12 and The day part should be between 1 to 31")
        return birth

    @validator("ID")
    def validate_id(cls,id):
        pattern = r"^[1-9]\d{9}$"
        if not re.match(pattern ,id) or len(id) != 10:
            raise ValueError("Invalid ID , ID should be have 10 digit")
        return id
    
    
    @validator("BornCity")
    def validate_borncity(cls,borncity):
        pattern = r"^(ارومیه|تبریز|اردبیل|رشت|ساری|گرگان|بجنورد|مشهد|سمنان|تهران|قزوین|زنجان|سنندج|همدان|اراک|قم|بیرجند|یزد|اصفهان|خرم آباد|ایلام|کرمانشاه|کرمان|زاهدان|بندرعباس|شیراز|یاسوج|شهرکرد|اهواز|بوشهر)$"
        if not re.match(pattern ,borncity):
            raise ValueError("Invalid BornCity , BornCity should one of the capital of the content")
        return borncity
    
    @validator("Address")
    def validate_address(cls,address):
        pattern = r"^[آ-ی\s\d,.]{1,100}$"
        if not re.match(pattern ,address) or len(address) > 100:
            raise ValueError("Invalid Address , Address should be persian and have at least 100 characters")
        return address
  
    @validator("PostalCode")
    def validate_post(cls,post):
        pattern = r"^\d{10}$"
        if not re.match(pattern ,post) or len(post) != 10:
            raise ValueError("Invalid PostalCode , PostalCode should be digit and have 10 character")
        return post

    @validator("CPhone")
    def validate_cphone(cls,cphone):
        pattern = r"^09\d{9}$"
        if not re.match(pattern ,cphone) or len(cphone) != 11:
            raise ValueError("Invalid CPhone , CPhone should be digit and start with '09' and have 11 digit")
        return cphone
    
    @validator("HPhone")
    def validate_hphone(cls,hphone):
        pattern = r"^(021|026|025|024|023|022|028|071|072|073|074|075|076|077|078|079|081|082|083|084|085|086|087|088|089|031|032|033|034|035|036|037|038|041|042|043|044|045|046|047|051|052|053|054|055|061|062|063|064|065|066|067)\d{8}$"
        if not re.match(pattern ,hphone) or len(hphone) != 11:
            raise ValueError("Invalid HPhone , HpHone should be digit and have 11 digit and should be written with the rules")
        return hphone

    @validator("Department")
    def validate_depart(cls,depart):
        pattern = r"^(علوم اجتماعی|مدیریت|علوم پایه|فنی و مهندسی|علوم انسانی|هنر|پزشکی|حقوق|دامپزشکی)$"
        if not re.match(pattern ,depart):
            raise ValueError("Invalid Department , Department should be one of the list of departments")
        return depart
        
    @validator("Major")
    def validate_major(cls,major):
        pattern = r"^(مهندسی برق|مهندسی کامپیوتر|مهندسی مکانیک|مهندسی عمران|مهندسی شیمی|مهندیس صنایع|مهندسی مواد|مهندسی نقشه برداری|مهندسی نفت|مهندسی هوافضا|مهندسی پزشکی |مهندسی راه آهن|مهندسی معدن|مهندسی کشاورزی|مهندسی نساجی|مهندسی آب|مهندسی خاک|مهندسی معماری)$"
        if not re.match(pattern ,major):
            raise ValueError("Invalid Major , Major should be one of the list of major")
        return major    



#DARS


class Dars(BaseModel):
    CID : str
    CName: str
    Department : str
    credit : int

     
    @validator("CID")
    def validate_cid(cls,cid):
        pattern = r"^\d{5}"
        if not re.match(pattern , cid) or len(cid) != 5:
            raise ValueError("Invalid CID , CID should have 5 digit")
        return cid
    
    @validator("CName")
    def validate_cname(cls,cname):
        pattern =  r"^[آ-ی]{1,25}$"
        if not re.match(pattern ,cname) or len(cname) > 25:
            raise ValueError("Invalid CName , CName should have at least 25 character and should be persian")
        return cname
    
    @validator("Department")
    def validate_depart(cls,depart):
        pattern =  r"^(علوم اجتماعی|مدیریت|علوم پایه|فنی و مهندسی|علوم انسانی|هنر|پزشکی|حقوق|دامپزشکی)$"
        if not re.match(pattern ,depart):
            raise ValueError("Invalid Department , Department should be one of the list of departments")
        return depart
    
    @validator("credit")
    def validate_credit(cls,credit):
        pattern = r"^[1-4]$"
        if not re.match(pattern , str(credit)) or credit < 1 or credit > 4:
            raise ValueError("Invalid Credit , credit should be between 1 and 4")
        return credit