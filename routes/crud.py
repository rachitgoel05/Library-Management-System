from fastapi import FastAPI, Request,APIRouter
from fastapi.responses import HTMLResponse 
from models.model import Student
from config.db import conn
from schemas.student import studentEntity,studentsEntity
import json
from bson import ObjectId

student = APIRouter()

@student.get("/allstudents", response_class=HTMLResponse)
async def get_all():
    try:
        docs = conn.LibraryManagementSystem.students.find({})
        new_docs = []
        if docs:
            for doc in docs:
                new_docs.append(studentEntity(doc))
            return json.dumps(new_docs)
    except Exception as e:
        print(e)
@student.get("/student/{id}", response_class=HTMLResponse)
async def find_one(id: str):
    try:
        doc = await conn.LibraryManagementSystem.students.find_one({
            "_id": ObjectId(id)
        })
        if doc:
            new_docs = []
            new_docs.append(studentEntity(doc))
            return json.dumps(new_docs)
    except Exception as e:
        print(e)

@student.post("/insertStudent", response_class=HTMLResponse)
async def find_one(student : Student):
    try:
        # doc = conn.LibraryManagementSystem.students.insert_one(dict(student))
        doc = await conn.LibraryManagementSystem.students.insert_one(student.dict())
        return json.dumps({"inserted_id":str(doc.inserted_id)})
    except Exception as e:
        print(e)

@student.put("/update_student/{id}", response_class=HTMLResponse)
async def update_one(id: str, student : Student):
    try:
        new_student = { "$set": dict(student) }
        doc = await conn.LibraryManagementSystem.students.update_one({
            "_id": ObjectId(id)
        }, new_student)
        return json.dumps({"message":"Updated"})
    except Exception as e:
        print(e)
@student.delete("/delete_student/{id}", response_class=HTMLResponse)
async def delete_one(id: str):
    student = await conn.LibraryManagementSystem.students.find_one({"_id": ObjectId(id)})
    try:
        if student:
            doc = await conn.LibraryManagementSystem.students.delete_one({
                "_id": ObjectId(id)
            })
            return json.dumps({"message":"Deleted"})
    except Exception as e:
        print(e)


