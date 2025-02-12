import requests
import os
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


UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")


def get_chess_image(orientation="landscape"):
    """
    Retrieves a random chess-themed image from the Unsplash API.
    orientation: "landscape" (desktop) or "portrait" (mobile)
    """
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": "chess",
        "orientation": orientation,
        "client_id": UNSPLASH_ACCESS_KEY,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["urls"]["regular"]
    except Exception as e:
        logger.info(f"❌ Unsplash API Error: {e}")
        return None
