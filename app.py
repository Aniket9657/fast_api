from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
students = {}







class Student(BaseModel):
    name: str
    age: int
    grade: str

@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    students[student_id] = student
    return students[student_id]



@app.get("students/{student_id}")
def get_student(student_id:int)
    return students.get(student_id,{"error": "Notfound"})



@app.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
    if student_id in students:
        students[student_id]=student
        return students[student_id]
    else :
        return {"error": "Student not found"}
    

@app.delete("/students/{studenr_id}")
def delete_student(student_id:int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted SUccessfully"}
    else :
        return {"error": "Student not found"}


