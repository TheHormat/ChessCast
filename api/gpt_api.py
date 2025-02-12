import os
import openai
from core.database import get_user_language
from core.languages import GPT_PROMPTS

# ✅ OpenAI API açarını yükləyirik
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ OpenAI müştərisini yaradaraq API açarını təyin edirik
client = openai.OpenAI(api_key=OPENAI_API_KEY)


async def get_chess_fact(user_id):
    try:
        print("📡 Sending a request to the GPT API...")

        # ✅ Get user's language from MongoDB
        user_lang = get_user_language(user_id)

        # ✅ If no language is found, English will be used as the default.
        prompt = GPT_PROMPTS.get(user_lang, GPT_PROMPTS["en"])

        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}],
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"❌ GPT API Error: {e}")
        return "⚠️ Could not connect to GPT API. Please check again later!"
