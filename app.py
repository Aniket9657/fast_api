from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()

students = {}

class Student(BaseModel):
    name: str 
    age :int
    grade : str 


@app.post("/students/{student_id}")
def create_student(student_id: int ,student: Student):
    students[student_id]= student
    return students[student_id]


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return students.get(student_id,{"error":"Not found"})
