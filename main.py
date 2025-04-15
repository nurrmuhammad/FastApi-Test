from fastapi import FastAPI, APIRouter
from data import school_db,student_db
from model import School,Student
app = FastAPI()

router = APIRouter(
    prefix="/api",
)

school_data:dict = {}
student_data:dict = {}

@router.get("/school")
async def school():
    return{"data":school_db}

@router.get("/student")
async def student():
    return {"data":student_db}

@router.post("/school-create")
async def school_create(schools:School):
    school["title"] = schools.title
    school["room"] = schools.room
    school["teacher"] = schools.teacher
    return {"data":school_data}

@router.post("/student-create")
async def student_create(students:Student):
    student["name"] = students.name
    student["email"] = students.email
    student["room_id"] = students.room_id
    student["since"] = students.since
    return {"data":student_data}

@router.get("/school/{school_name}")
async def school_name(school_name: str):
    for school in school_db:
        if school["title"].lower() == school_name.lower():
            return {"data": school}
    return {"error": "School not found"}

@router.get("/student/{student_name}")
async def student_name(student_name: str):
    for student in student_db:
        if student["name"].lower() == student_name.lower():
            return {"data": student}
    return {"error": "Student not found"}


app.include_router(router)