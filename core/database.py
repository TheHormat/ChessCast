from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

from api.chess_com_api import get_chess_com_rating
from api.lichess_api import get_lichess_rating

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

# ✅ Define Database and Collection
db = client["chesscast"]  # ChessCast DB
users_collection = db["users"]  # Collection for users


def add_user(user_id):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one(
            {
                "user_id": user_id,
                "first_joined": datetime.now(timezone.utc),  # First join date
                "language": "en",
                "user_rating": None,
            }
        )


# ✅ Remove user
def remove_user(user_id):
    users_collection.delete_one({"user_id": user_id})


# ✅ Check if the user is registered
def is_user_registered(user_id):
    return users_collection.find_one({"user_id": user_id}) is not None


# ✅ Get the total number of users
def get_user_count():
    return users_collection.count_documents({})


def get_user_language(user_id):
    user_data = db.users.find_one({"user_id": user_id})
    return user_data["language"] if user_data and "language" in user_data else "en"


def update_user_rating(user_id, rating):
    """
    Updates the user's rating.
    """
    users_collection.update_one(
        {"user_id": user_id}, {"$set": {"user_rating": rating}}, upsert=True
    )


def get_user_rating(user_id):
    """
    Returns the user's rating.
    """
    user = users_collection.find_one({"user_id": user_id}, {"user_rating": 1, "_id": 0})
    return user.get("user_rating") if user else None


def get_top_players(limit=10):
    """
    Returns the top players with the highest ratings.
    """
    top_players = (
        users_collection.find(
            {"user_rating": {"$ne": None}},  # Get users who have a rating
            {
                "user_id": 1,
                "chess_username": 1,
                "user_rating": 1,
                "_id": 0,
            },  # Select required fields
        )
        .sort("user_rating", -1)  # Sort by rating in descending order
        .limit(limit)  # Apply limit
    )

    return list(top_players)


def update_user_rating_from_api(user_id):
    """
    Updates the user's rating from Chess.com or Lichess API and stores it in MongoDB.
    """
    user = users_collection.find_one({"user_id": user_id}, {"chess_username": 1})

    if not user or "chess_username" not in user:
        return None  # Do nothing if the username is missing

    username = user["chess_username"]

    # Get user's rating from Chess.com API
    chess_rating = get_chess_com_rating(username)

    # Get user's rating from Lichess API
    lichess_rating = get_lichess_rating(username)

    # Take the highest rating
    best_rating = max(filter(None, [chess_rating, lichess_rating]))

    if best_rating:
        users_collection.update_one(
            {"user_id": user_id}, {"$set": {"user_rating": best_rating}}
        )

    return best_rating  # Returns the updated rating
