import requests
from core.languages import MESSAGES


# ✅ Function to pull tournament data from Lichess API
def get_lichess_tournaments():
    url = "https://lichess.org/api/tournament"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, str):
            import json

            data = json.loads(data)

        if "created" not in data:
            print("⚠️ Unexpected API Response:", data)
            return None

        return data["created"]

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Lichess API error: {e}")
        return None


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

        if user_rating and rating_limit is not None:
            if user_rating > rating_limit:
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

        if "error" in data:
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Lichess API error: {e}")
        return None


def get_lichess_rating(username):
    url = f"https://lichess.org/api/user/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # We take the highest rating (Blitz and Bullet)
        blitz_rating = data.get("perfs", {}).get("blitz", {}).get("rating", None)
        bullet_rating = data.get("perfs", {}).get("bullet", {}).get("rating", None)

        return max(filter(None, [blitz_rating, bullet_rating]))

    except requests.exceptions.RequestException:
        return None


def get_lichess_daily_puzzle():
    """
    Fetches the daily chess puzzle from the Lichess API.
    """
    url = "https://lichess.org/api/puzzle/daily"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print(f"✅ Response from API: {data}")

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

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Lichess API Error: {e}")
        return None
