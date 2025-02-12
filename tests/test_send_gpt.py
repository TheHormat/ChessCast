import asyncio
from core.bot import send_chess_fact

loop = asyncio.get_event_loop()
loop.run_until_complete(send_chess_fact())