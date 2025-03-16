import requests
from core.languages import MESSAGES
import httpx
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


# ✅ Function to pull tournament data from Lichess API
def get_lichess_tournaments():
    url = "https://lichess.org/api/tournament"
    try:
        return _extracted_from_get_lichess_tournaments_4(url)
    except requests.exceptions.RequestException as e:
        logger.info(f"⚠️ Lichess API error: {e}")
        return None


# TODO Rename this here and in `get_lichess_tournaments`
def _extracted_from_get_lichess_tournaments_4(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, str):
        import json

        data = json.loads(data)

    if "created" not in data:
        logger.info("⚠️ Unexpected API Response:", data)
        return None

    return data["created"]


# ✅ The function of filtering tournaments according to the user's rating
def filter_tournaments_by_rating(tournaments, user_rating=None, user_lang="az"):
    message = MESSAGES[user_lang]["lichess_arena_header"]
    count = 0

    if not isinstance(tournaments, list):
        return MESSAGES[user_lang]["lichess_arena_no_data"]

    for tournament in tournaments:
        if not isinstance(tournament, dict):
            continue

        name = tournament.get(
            "fullName",
            "None Turnir" if user_lang == "az" else "Unknown Tournament",
        )
        link = f"https://lichess.org/tournament/{tournament.get('id', '')}"
        rating_limit = tournament.get("maxRating", {}).get("rating", None)
        starts_in_seconds = tournament.get("secondsToStart", 0)
        minutes_to_start = starts_in_seconds // 60

        if user_rating and rating_limit is not None and user_rating > rating_limit:
            continue

        message += f"🔹 [{name}]({link}) {MESSAGES[user_lang]['lichess_arena_starts_in'].format(minutes_to_start)}\n"
        count += 1

        if count == 5:
            break

    if count == 0:
        message += MESSAGES[user_lang]["lichess_arena_no_tournaments"]

    return message


def get_lichess_profile(username):
    url = f"https://lichess.org/api/user/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return None if "error" in data else data
    except requests.exceptions.RequestException as e:
        logger.info(f"⚠️ Lichess API error: {e}")
        return None


async def get_lichess_rating(username):
    url = f"https://lichess.org/api/user/{username}"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

        # En yüksek Blitz ve Bullet rating'ini al
        blitz_rating = data.get("perfs", {}).get("blitz", {}).get("rating", None)
        bullet_rating = data.get("perfs", {}).get("bullet", {}).get("rating", None)

        return max(filter(None, [blitz_rating, bullet_rating]))

    except httpx.RequestError:
        return None


def get_lichess_daily_puzzle():
    """
    Fetches the daily chess puzzle from the Lichess API.
    """
    url = "https://lichess.org/api/puzzle/daily"
    try:
        return _extracted_from_get_lichess_daily_puzzle_7(url)
    except requests.exceptions.RequestException as e:
        logger.info(f"⚠️ Lichess API Error: {e}")
        return None


# TODO Rename this here and in `get_lichess_daily_puzzle`
def _extracted_from_get_lichess_daily_puzzle_7(url):
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    logger.info(f"✅ Response from API: {data}")

    puzzle_id = data.get("puzzle", {}).get("id", "None")  # Puzzle ID
    puzzle_rating = data.get("puzzle", {}).get("rating", "None")  # Difficulty level
    puzzle_plays = data.get("puzzle", {}).get(
        "plays", 0
    )  # How many times has the puzzle been played?
    puzzle_url = f"https://lichess.org/training/{puzzle_id}"

    return {
        "id": puzzle_id,
        "rating": puzzle_rating,
        "plays": puzzle_plays,
        "url": puzzle_url,
    }
