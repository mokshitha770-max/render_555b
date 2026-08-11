 from fastapi import fastAPI
from pydantic import Basemodel

app = fastAPI(title="student details management API")

# 1.in memory Database
students_db = {
    1: {"name":"mokshitha","age":21,"course":"Data analytics"},
    2: {"name":"hemalatha","age":20,"course":"Data science"},
    3: {"name":"uma","age":21,"course":"AI & ML"},
}

#2.data visualization model
class student(BaseModel):
    name: str
    age: int
    course: str


==========================================
READ (GET) - View All or Filter by Course
==========================================
@app.get("/students/")
def get_students(course: str = None):
    if course:
        filtered = {
            s_id: s
            for s_id, s in students_db.items()
            if s["course"].lower() == course.lower()
        }
        return filtered

    return students_db

    
