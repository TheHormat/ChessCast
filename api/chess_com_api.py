import requests
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


# ✅ Function to retrieve user profile from Chess.com API
def get_chess_com_profile(username):
    url = f"https://api.chess.com/pub/player/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.info(f"⚠️ Chess.com Profil API hatası: {e}")
        return None


# ✅ Function to retrieve user rating and game information from Chess.com API
def get_chess_com_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.info(f"⚠️ Chess.com Rating API hatası: {e}")
        return None


def get_chess_com_rating(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # We take the highest rating (Blitz and Bullet)
        blitz_rating = data.get("chess_blitz", {}).get("last", {}).get("rating", None)
        bullet_rating = data.get("chess_bullet", {}).get("last", {}).get("rating", None)

        return max(
            filter(None, [blitz_rating, bullet_rating])
        )  # We return at the highest price

    except requests.exceptions.RequestException:
        return None
