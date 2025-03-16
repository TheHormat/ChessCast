from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Bot
from api.gpt_api import get_chess_fact
from api.unsplash_api import get_chess_image
from core.scheduler import schedule_task
from core.static_facts import CHESS_FACTS
import schedule
import asyncio
import nest_asyncio
import os
import random
import logging
from dotenv import load_dotenv
from core.languages import MESSAGES
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler,
)

from core.database import (
    add_user,
    get_all_user_ids,
    init_db,
    update_user_language,
    get_top_players,
    get_user_language,
    is_user_registered,
    remove_user,
    get_user_data,
    update_user_rating,
)

from api.chess_com_api import (
    get_chess_com_profile,
    get_chess_com_rating,
    get_chess_com_stats,
)

from api.lichess_api import (
    filter_tournaments_by_rating,
    get_lichess_daily_puzzle,
    get_lichess_tournaments,
    get_lichess_profile,
    get_lichess_rating,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("bot.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
nest_asyncio.apply()


async def get_message(user_id, key):
    user_lang = await get_user_language(user_id)
    return MESSAGES.get(user_lang, MESSAGES["en"]).get(key, "Message not found")


async def set_language_command(update: Update, context: CallbackContext) -> None:
    """
    Sends an inline keyboard to the user to select a language.
    """
    user_id = update.effective_chat.id
    user_data = await get_user_data(user_id, ["language"])
    user_lang = user_data.get("language", "en")

    keyboard = [
        [
            InlineKeyboardButton("🇦🇿 Azərbaycan", callback_data="set_lang_az"),
            InlineKeyboardButton("🇬🇧 English", callback_data="set_lang_en"),
        ],
        [
            InlineKeyboardButton("🇷🇺 Русский", callback_data="set_lang_ru"),
            InlineKeyboardButton("🇹🇷 Türkçe", callback_data="set_lang_tr"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Language selection message based on the user's current language
    if user_lang == "en":
        message_text = "🌍 *Please select your language:*"
    elif user_lang == "az":
        message_text = "🌍 *Zəhmət olmasa, dil seçin:*"
    elif user_lang == "ru":
        message_text = "🌍 *Пожалуйста, выберите ваш язык:*"
    else:
        message_text = "🌍 *Lütfen dilinizi seçin:*"

    await update.message.reply_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode="Markdown",
    )


def get_language_from_callback(data):
    lang_map = {
        "set_lang_az": "az",
        "set_lang_en": "en",
        "set_lang_ru": "ru",
        "set_lang_tr": "tr",
    }
    return lang_map.get(data)


async def language_callback(update: Update, context: CallbackContext) -> None:
    """
    Handles the user's language selection from the inline keyboard.
    """
    query = update.callback_query
    user_id = query.from_user.id
    selected_lang = query.data

    new_lang = get_language_from_callback(selected_lang)
    if not new_lang:
        return

    # ✅ PostgreSQL veritabanında kullanıcı dilini güncelle
    await update_user_language(user_id, new_lang)

    # Confirm language change in the selected language
    confirmation_message = MESSAGES[new_lang]["language_set"]

    await query.answer()
    await query.edit_message_text(confirmation_message)

    logger.info(f"✅ User {user_id} changed language to {new_lang}")


# ✅ `/start` command: Registers the user and sends a static welcome message + random chess information
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    # ✅ If the user is logging in for the first time, register and send static facts
    if not await is_user_registered(user_id):
        await add_user(user_id)
        await update.message.reply_text(MESSAGES[user_lang]["start_welcome"])

        # ✅ Send random information from CHESS_FACTS for new user
        fact_list = CHESS_FACTS.get(user_lang, CHESS_FACTS["en"])  # Default English
        fact = random.choice(fact_list)
        await update.message.reply_text(fact, parse_mode="Markdown")
    else:
        await update.message.reply_text(MESSAGES[user_lang]["start_already_registered"])


async def about_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    about_text = MESSAGES[user_lang]["about"]

    await update.message.reply_text(
        about_text, parse_mode="Markdown", disable_web_page_preview=True
    )


async def lichess_arena_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    user_input = context.args

    if user_input and not user_input[0].isdigit():
        await update.message.reply_text(
            MESSAGES[user_lang]["lichess_arena_error"],
            parse_mode="Markdown",
        )
        return

    user_rating = int(user_input[0]) if user_input else None

    tournaments = get_lichess_tournaments()
    if not tournaments:
        await update.message.reply_text(MESSAGES[user_lang]["lichess_arena_no_data"])
        return

    message = filter_tournaments_by_rating(tournaments, user_rating, user_lang)

    await update.message.reply_text(
        message, parse_mode="Markdown", disable_web_page_preview=True
    )


async def lichess_profile_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    if not context.args:
        await update.message.reply_text(
            MESSAGES[user_lang]["lichess_profile_usage"], parse_mode="Markdown"
        )
        return

    username = context.args[0]
    profile = get_lichess_profile(username)

    if not profile:
        await update.message.reply_text(
            MESSAGES[user_lang]["lichess_profile_not_found"].format(username),
            parse_mode="Markdown",
        )
        return

    rating_blitz = profile.get("perfs", {}).get("blitz", {}).get("rating", "Unknown")
    rating_bullet = profile.get("perfs", {}).get("bullet", {}).get("rating", "Unknown")
    rating_rapid = profile.get("perfs", {}).get("rapid", {}).get("rating", "Unknown")

    games_played = profile.get("count", {}).get("all", "Unknown")
    games_won = profile.get("count", {}).get("win", 0)
    games_lost = profile.get("count", {}).get("loss", 0)
    games_drawn = profile.get("count", {}).get("draw", 0)

    win_percentage = (
        round((games_won / games_played) * 100, 2)
        if isinstance(games_played, int) and games_played > 0
        else "Unknown"
    )

    message = (
        MESSAGES[user_lang]["lichess_profile_header"].format(username)
        + MESSAGES[user_lang]["rating_bullet"].format(rating_bullet)
        + "\n"
        + MESSAGES[user_lang]["rating_blitz"].format(rating_blitz)
        + "\n"
        + MESSAGES[user_lang]["rating_rapid"].format(rating_rapid)
        + "\n\n"
        + MESSAGES[user_lang]["total_games"].format(games_played)
        + "\n\n"
        + MESSAGES[user_lang]["games_won"].format(games_won, win_percentage)
        + "\n\n"
        + MESSAGES[user_lang]["games_lost"].format(games_lost)
        + "\n\n"
        + MESSAGES[user_lang]["games_drawn"].format(games_drawn)
        + "\n\n"
        + MESSAGES[user_lang]["view_profile"].format(
            f"https://lichess.org/@/{username}"
        )
    )

    await update.message.reply_text(
        message, parse_mode="Markdown", disable_web_page_preview=True
    )


# Chess.com
async def chess_com_profile_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    if not context.args:
        await update.message.reply_text(
            MESSAGES[user_lang]["chess_profile_usage"], parse_mode="Markdown"
        )
        return

    username = context.args[0]
    profile = get_chess_com_profile(username)

    if not profile:
        await update.message.reply_text(
            MESSAGES[user_lang]["chess_profile_not_found"].format(username),
            parse_mode="Markdown",
        )
        return

    stats = get_chess_com_stats(username)
    game_modes = ["chess_blitz", "chess_bullet", "chess_rapid", "chess_daily"]

    total_games = 0
    total_wins = 0
    total_losses = 0
    total_draws = 0
    ratings = {}

    for mode in game_modes:
        mode_data = stats.get(mode, {})
        ratings[mode] = mode_data.get("last", {}).get("rating", "Unknown")
        record = mode_data.get("record", {})
        total_wins += record.get("win", 0)
        total_losses += record.get("loss", 0)
        total_draws += record.get("draw", 0)

    total_games = total_wins + total_losses + total_draws
    win_percentage = (
        round((total_wins / total_games) * 100, 2) if total_games > 0 else "Unknown"
    )

    profile_picture = profile.get("avatar", None)

    message = (
        MESSAGES[user_lang]["chess_profile_header"].format(username)
        + MESSAGES[user_lang]["rating_bullet"].format(ratings["chess_bullet"])
        + "\n"
        + MESSAGES[user_lang]["rating_blitz"].format(ratings["chess_blitz"])
        + "\n"
        + MESSAGES[user_lang]["rating_rapid"].format(ratings["chess_rapid"])
        + "\n"
        + MESSAGES[user_lang]["rating_daily"].format(ratings["chess_daily"])
        + "\n\n"
        + MESSAGES[user_lang]["total_games"].format(total_games)
        + "\n\n"
        + MESSAGES[user_lang]["games_won"].format(total_wins, win_percentage)
        + "\n\n"
        + MESSAGES[user_lang]["games_lost"].format(total_losses)
        + "\n\n"
        + MESSAGES[user_lang]["games_drawn"].format(total_draws)
        + "\n\n"
        + MESSAGES[user_lang]["view_profile"].format(
            f"https://www.chess.com/member/{username}"
        )
    )

    if profile_picture:
        await update.message.reply_photo(
            photo=profile_picture, caption=message, parse_mode="Markdown"
        )
    else:
        await update.message.reply_text(
            message, parse_mode="Markdown", disable_web_page_preview=True
        )


async def donate_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    await update.message.reply_text(
        MESSAGES[user_lang]["donate_message"],
        parse_mode="Markdown",
        disable_web_page_preview=True,
    )


async def set_rating_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    if not context.args:
        await update.message.reply_text(
            MESSAGES[user_lang]["set_rating_usage"], parse_mode="Markdown"
        )
        return

    username = context.args[0]

    lichess_rating = await get_lichess_rating(username)
    chesscom_rating = await get_chess_com_rating(username)

    print(f"Lichess Rating for {username}: {lichess_rating}")
    print(f"Chess.com Rating for {username}: {chesscom_rating}")

    if lichess_rating is None and chesscom_rating is None:
        await update.message.reply_text(
            MESSAGES[user_lang]["set_rating_not_found"].format(username=username),
            parse_mode="Markdown",
        )
        return

    max_rating = max(filter(None, [lichess_rating, chesscom_rating]))

    await update_user_rating(user_id, max_rating, username)

    await update.message.reply_text(
        MESSAGES[user_lang]["set_rating_success"].format(
            username=username, rating=max_rating
        ),
        parse_mode="Markdown",
    )


async def topplayers_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    top_players = await get_top_players(limit=10)

    if not top_players:
        await update.message.reply_text(MESSAGES[user_lang]["topplayers_no_data"])
        return

    message = f"<b>🏆 {MESSAGES[user_lang]['topplayers_header']}</b>\n\n"

    for index, player in enumerate(top_players, start=1):
        user_id = player["user_id"]

        updated_rating = await update_user_rating(user_id)

        username = player.get("chess_username", "Unknown")
        rating = updated_rating or player.get("user_rating", "None")

        message += f"{index}. <b>{username}</b> - {rating} Elo\n"

    await update.message.reply_text(message, parse_mode="HTML")


async def unsubscribe(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    if await is_user_registered(user_id):
        await remove_user(user_id)
        await update.message.reply_text(MESSAGES[user_lang]["unsubscribe_success"])
    else:
        await update.message.reply_text(MESSAGES[user_lang]["unsubscribe_already"])


async def puzzle_command(update: Update, context: CallbackContext) -> None:
    """
    Sends the daily chess puzzle to the user.
    """
    logger.info("🔍 /puzzle command called.")

    user_id = update.effective_chat.id
    user_lang = await get_user_language(user_id)

    puzzle = get_lichess_daily_puzzle()

    if not puzzle:
        logger.info("⚠️ Lichess API did not respond.")
        await update.message.reply_text(MESSAGES[user_lang]["puzzle_error"])
        return

    logger.info(f"✅ Puzzle found: {puzzle['id']}")

    message = MESSAGES[user_lang]["puzzle_message"].format(
        url=puzzle["url"], rating=puzzle["rating"], plays=puzzle["plays"]
    )

    await update.message.reply_text(
        message, parse_mode="Markdown", disable_web_page_preview=True
    )


async def send_daily_puzzle():
    """
    Sends the daily puzzle to all users every day.
    """
    users = await get_all_user_ids()

    if not users:
        logger.info("⚠️ No users found.")
        return

    puzzle = get_lichess_daily_puzzle()
    if not puzzle:
        logger.info("⚠️ Could not retrieve the daily puzzle.")
        return

    # Mesajları hazırla
    message_az = MESSAGES["az"]["puzzle_message"].format(
        url=puzzle["url"], rating=puzzle["rating"], plays=puzzle["plays"]
    )
    message_en = MESSAGES["en"]["puzzle_message"].format(
        url=puzzle["url"], rating=puzzle["rating"], plays=puzzle["plays"]
    )

    # Mesajları kullanıcıların diline göre gönder
    for user_id in users:
        try:
            user_lang = await get_user_language(user_id)
            message = message_az if user_lang == "az" else message_en
            await bot.send_message(
                chat_id=user_id,
                text=message,
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
            logger.info(f"✅ Daily puzzle sent: {user_id}")
        except Exception as e:
            logger.info(f"❌ Failed to send message ({user_id}): {e}")


async def send_daily_chess_images():
    """
    Sends 2 desktop and 3 mobile chess images to all users every day.
    """
    users = await get_all_user_ids()

    if not users:
        logger.info("⚠️ No users found.")
        return

    # Görselleri hazırla
    desktop_images = [get_chess_image("landscape") for _ in range(2)]
    mobile_images = [get_chess_image("portrait") for _ in range(3)]

    all_images = desktop_images + mobile_images  # ✅ 5 images

    for image_url in all_images:
        if not image_url:
            logger.info("⚠️ No image found, continuing...")
            continue

        for user_id in users:
            try:
                user_lang = await get_user_language(user_id)
                message = MESSAGES[user_lang]["daily_chess_images"]
                await bot.send_photo(chat_id=user_id, photo=image_url, caption=message)
                logger.info(f"✅ Image sent: {user_id}")
            except Exception as e:
                logger.info(f"❌ Failed to send message ({user_id}): {e}")


# ✅ Function to send a message from GPT-4 to all users
async def send_chess_fact():
    """
    Sends a chess fact to all users.
    """
    users = await get_all_user_ids()

    if not users:
        logger.info("⚠️ No users found.")
        return

    for user_id in users:
        try:
            user_lang = await get_user_language(user_id)
            intro_message = MESSAGES[user_lang]["intro_gpt_message"]

            # Ön mesajı gönder
            await bot.send_message(
                chat_id=user_id, text=intro_message, parse_mode="Markdown"
            )

            # Satranç bilgisini al ve gönder
            fact = await get_chess_fact(user_id)
            await bot.send_message(chat_id=user_id, text=fact, parse_mode="Markdown")
            logger.info(f"✅ Chess fact sent: {user_id}")
        except Exception as e:
            logger.info(f"❌ Failed to send message ({user_id}): {e}")


# ✅ Secure messaging function for users
async def send_message(user_id, text):
    try:
        await bot.send_message(chat_id=user_id, text=text, parse_mode="Markdown")
    except Exception as e:
        logger.info(f"Message could not be sent: ({user_id}): {e}")


# ✅ Starting the bot
async def main():
    await init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    try:
        await setup_handlers(app)
        asyncio.create_task(setup_schedulers())  # ✅ Run scheduler in background

        logger.info("Bot working... 🚀")  # This should now print!

        await app.run_polling(drop_pending_updates=True)
    finally:
        await app.shutdown()


async def setup_handlers(app: Application):
    """Sets up command and callback query handlers."""
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("language", set_language_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(CommandHandler("puzzle", puzzle_command))
    app.add_handler(CommandHandler("setrating", set_rating_command))
    app.add_handler(CommandHandler("topplayers", topplayers_command))
    app.add_handler(CommandHandler("lichessarena", lichess_arena_command))
    app.add_handler(CommandHandler("lichessprofile", lichess_profile_command))
    app.add_handler(CommandHandler("chessprofile", chess_com_profile_command))
    app.add_handler(CommandHandler("donate", donate_command))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe))
    app.add_handler(CallbackQueryHandler(language_callback, pattern="^set_lang_"))


async def setup_schedulers():
    """Schedules daily tasks at specific times (only once)."""
    if schedule.get_jobs():
        logger.info("⚠️ Scheduler already initialized, skipping duplicate scheduling.")
        return

    schedule.every().day.at("09:00").do(
        lambda: asyncio.create_task(send_daily_puzzle())
    )
    schedule.every().day.at("18:00").do(
        lambda: asyncio.create_task(send_daily_chess_images())
    )

    logger.info("✅ Scheduled daily tasks at 09:00 and 18:00")

    # ✅ Wait for the schedule task instead of background task
    await schedule_task()


# ✅ Start Bot
if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(main())
