from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

from api.chess_com_api import get_chess_com_rating
from api.lichess_api import get_lichess_rating

# ✅ Load environment variables
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in the environment variables.")

client = MongoClient(MONGO_URI)
db = client["chesscast"]


def get_user_collection():
    return db["users"]


# ✅ Add a new user to the database
def add_user(user_id, language="en"):
    users_collection = get_user_collection()

    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one(
            {
                "user_id": user_id,
                "first_joined": datetime.now(timezone.utc),
                "language": language,
                "user_rating": None,
                "chess_username": None,
            }
        )


# ✅ Remove user from the database
def remove_user(user_id):
    get_user_collection().delete_one({"user_id": user_id})


# ✅ Check if a user is registered
def is_user_registered(user_id):
    return get_user_collection().find_one({"user_id": user_id}) is not None


# ✅ Get total number of users
def get_user_count():
    return get_user_collection().count_documents({})


# ✅ Get user language, defaulting to "en"
def get_user_language(user_id):
    user_data = get_user_collection().find_one(
        {"user_id": user_id}, {"language": 1, "_id": 0}
    )
    return user_data.get("language", "en") if user_data else "en"


# ✅ Update user's rating
def update_user_rating(user_id, rating):
    if rating is None:
        return

    get_user_collection().update_one(
        {"user_id": user_id}, {"$set": {"user_rating": rating}}, upsert=True
    )


# ✅ Get user rating
def get_user_rating(user_id):
    user = get_user_collection().find_one(
        {"user_id": user_id}, {"user_rating": 1, "_id": 0}
    )
    return user.get("user_rating") if user else None


# ✅ Get top players with highest ratings
async def get_top_players(limit=10):
    return list(
        get_user_collection()
        .find(
            {"user_rating": {"$ne": None}},
            {"user_id": 1, "chess_username": 1, "user_rating": 1, "_id": 0},
        )
        .sort("user_rating", -1)
        .limit(limit)
    )


# ✅ Update user's rating using external APIs
async def update_user_rating_from_api(user_id):
    users_collection = get_user_collection()
    user = users_collection.find_one({"user_id": user_id}, {"chess_username": 1})

    if not user or "chess_username" not in user:
        return None

    username = user["chess_username"]

    # Fetch rating from both APIs
    ratings = [
        get_chess_com_rating(username),
        get_lichess_rating(username),
    ]

    best_rating = max(filter(None, ratings), default=None)

    if best_rating is not None:
        users_collection.update_one(
            {"user_id": user_id}, {"$set": {"user_rating": best_rating}}
        )

    return best_rating
