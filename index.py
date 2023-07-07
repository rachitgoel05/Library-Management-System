from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse 
from routes.crud import student

app = FastAPI()
app.include_router(student)

# from pydantic import BaseModel
# from pymongo import MongoClient
# import datetime

# client = MongoClient("mongodb+srv://CohortLearning:sEWwAgVz10B3PKkZ@cohort.wqg09zp.mongodb.net/")
# print(client)

# db = client.LibraryManagementSystem

# collection = db.students


# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.now(tz=datetime.timezone.utc),
# }
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print(post_id)