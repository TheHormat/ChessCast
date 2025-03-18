import os
import openai
import logging
import random
from core.database import get_user_language
from dotenv import load_dotenv
from core.languages import (
    GPT_PROMPTS,
    topics_by_language,
    topic_instruction_by_language,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)


async def get_chess_fact(user_id):
    try:
        logger.info("📡 Sending a request to the GPT API...")
        user_lang = await get_user_language(user_id)

        if not user_lang or user_lang not in GPT_PROMPTS:
            user_lang = "en"

        prompt_template = GPT_PROMPTS[user_lang]

        topics = topics_by_language.get(user_lang, topics_by_language["en"])
        selected_topic = random.choice(topics)

        topic_instruction = topic_instruction_by_language.get(
            user_lang, topic_instruction_by_language["en"]
        )

        prompt = (
            prompt_template
            + f"\n{topic_instruction}: **{selected_topic}**."
            + "\nRespond entirely in this language and do not use any other language."
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        logger.info(f"❌ GPT API Error: {e}")
        return "⚠️ Failed to connect to GPT API, please try again later!"
