import asyncio
import random
import schedule
import logging
from datetime import datetime, timedelta
from core.bot import send_chess_fact  # Import once at the top

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)


def get_random_times():
    """
    Generates two distinct random times between 08:00 and 22:00.
    """
    start_time = 8  # 08:00 AM
    end_time = 20  # 10:00 PM

    times = set()  # Use a set to avoid duplicates
    while len(times) < 2:
        hour = random.randint(start_time, end_time - 1)
        minute = random.randint(0, 59)
        times.add(f"{hour:02d}:{minute:02d}")

    return list(times)


def schedule_random_times():
    """
    Clears previous schedules and sets two new random times for daily chess facts.
    """
    schedule.clear()  # Remove previous schedules

    first_time, second_time = get_random_times()
    logger.info(f"📅 Scheduled chess facts at: {first_time}, {second_time}")

    # Schedule tasks safely
    schedule.every().day.at(first_time).do(
        lambda: asyncio.create_task(safe_send_fact())
    )
    schedule.every().day.at(second_time).do(
        lambda: asyncio.create_task(safe_send_fact())
    )


async def safe_send_fact():
    """
    Ensures send_chess_fact() runs without affecting the scheduler.
    """
    try:
        await send_chess_fact()
    except Exception as e:
        logger.error(f"⚠️ Error sending chess fact: {e}")


async def schedule_task():
    """
    Runs scheduled tasks and resets the schedule at midnight.
    """
    schedule_random_times()  # Initial schedule setup
    next_midnight = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.min.time()
    )

    while True:
        now = datetime.now()

        if now >= next_midnight:
            logger.info("🔄 Resetting schedule at midnight...")
            schedule_random_times()
            next_midnight = datetime.combine(
                now.date() + timedelta(days=1), datetime.min.time()
            )

        schedule.run_pending()
        await asyncio.sleep(60)  # Wait a minute before checking again
