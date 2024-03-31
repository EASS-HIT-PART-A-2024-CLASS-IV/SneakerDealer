from pymongo import MongoClient

from motor.motor_asyncio import AsyncIOMotorClient

mongo_uri = "mongodb+srv://admin:admin123123@cluster0.xrhcmq8.mongodb.net/?retryWrites=true&w=majority"

# Initialize the client to connect to your MongoDB cluster
client = AsyncIOMotorClient(mongo_uri)

# Connect to the specific database
database = client.Users_Database

# Connect to the specific collection
user_collection = database.get_collection("users_collection")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "hashed_password": user["hashed_password"]
    }

