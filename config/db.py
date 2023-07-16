from pymongo import MongoClient
import motor.motor_asyncio

MONGO_URI = "mongodb+srv://<username>:<password>@cohort.wqg09zp.mongodb.net"

conn = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
try:
    # Send a ping to confirm a successful connection
    conn.admin.command('ping')
    print("You have successfully connected to MongoDB!")
except Exception as e:
    print(e)

"mongodb+srv://CohortLearning:sEWwAgVz10B3PKkZ@cohort.wqg09zp.mongodb.net"