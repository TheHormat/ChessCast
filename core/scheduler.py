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
    start_time = 8
    end_time = 20
    times = set()
    while len(times) < 2:
        hour = random.randint(start_time, end_time - 1)
        minute = random.randint(0, 59)
        times.add(f"{hour:02d}:{minute:02d}")
    return list(times)


def schedule_random_times():
    """
    Daha önceki görevleri temizler ve yeni iki rastgele saat belirler.
    """
    from core.bot import send_chess_fact  

    schedule.clear()
    first_time, second_time = get_random_times()
    logger.info(f"📅 Rastgele saatler belirlendi: {first_time}, {second_time}")

    schedule.every().day.at(first_time).do(
        lambda: asyncio.create_task(send_chess_fact())
    )
    schedule.every().day.at(second_time).do(
        lambda: asyncio.create_task(send_chess_fact())
    )


async def schedule_task():
    schedule_random_times()
    next_midnight = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.min.time()
    )

    while True:
        now = datetime.now()

        if now >= next_midnight:
            logger.info("🔄 Gece yarısı program yenileniyor...")
            schedule_random_times()
            next_midnight = datetime.combine(
                now.date() + timedelta(days=1), datetime.min.time()
            )

        schedule.run_pending()
        await asyncio.sleep(60)
