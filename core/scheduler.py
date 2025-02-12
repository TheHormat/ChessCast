import asyncio
import random
import schedule
import logging
from datetime import datetime, timedelta

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
    Generates two random times for sending chess facts between 08:00 and 22:00.
    """
    start_time = 8  # AM 08:00
    end_time = 22  # PM 22:00

    first_hour = random.randint(start_time, end_time - 1)
    second_hour = random.randint(start_time, end_time - 1)

    # Ensure that the second hour is different
    while second_hour == first_hour:
        second_hour = random.randint(start_time, end_time - 1)

    first_time = f"{first_hour:02d}:{random.randint(0, 59):02d}"
    second_time = f"{second_hour:02d}:{random.randint(0, 59):02d}"

    return first_time, second_time


def schedule_random_times():
    """
    Clears previous schedules and sets two new random times for daily chess facts.
    """
    from core.bot import (
        send_chess_fact,
    )

    first_time, second_time = get_random_times()
    logger.info(f"📅 Random schedule set for today: {first_time}, {second_time}")

    schedule.clear()  # Remove previous schedules

    schedule.every().day.at(first_time).do(
        lambda: asyncio.create_task(send_chess_fact())
    )
    schedule.every().day.at(second_time).do(
        lambda: asyncio.create_task(send_chess_fact())
    )


async def schedule_task():
    """
    Runs scheduled tasks in a loop and updates the schedule at midnight.
    """
    next_midnight = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.min.time()
    )

    while True:
        now = datetime.now()

        # Reset schedule at midnight
        if now >= next_midnight:
            logger.info("🔄 Resetting schedule at midnight...")
            schedule_random_times()
            next_midnight = datetime.combine(
                now.date() + timedelta(days=1), datetime.min.time()
            )  # New day

        schedule.run_pending()
        await asyncio.sleep(60)
