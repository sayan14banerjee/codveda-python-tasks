from pymongo import MongoClient

# Local MongoDB connection (change if using Atlas)
MONGO_URI = "mongodb://localhost:27017/"

client = MongoClient(MONGO_URI)
db = client["blogsite_db"]

# Create collections
posts_collection = db["posts"]
print("✅ Connected to MongoDB:", db.name)