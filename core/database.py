import asyncpg
from dotenv import load_dotenv
from datetime import datetime, timezone
import os

# Load environment variables
load_dotenv()
POSTGRES_URI = os.getenv("POSTGRES_URI")

# Global connection pool
db_pool = None


async def init_db():
    global db_pool
    db_pool = await asyncpg.create_pool(dsn=POSTGRES_URI)


async def create_table():
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            first_joined TIMESTAMP,
            language VARCHAR(10),
            user_rating INTEGER,
            chess_username VARCHAR(100)
        )
        """
        )


async def add_user(user_id: int, language: str = "en"):
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
        INSERT INTO users (user_id, first_joined, language)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO NOTHING
        """,
            user_id,
            datetime.now(timezone.utc),
            language,
        )


async def update_user_language(user_id: int, language: str):
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
        INSERT INTO users (user_id, language)
        VALUES ($1, $2)
        ON CONFLICT (user_id) DO UPDATE SET language = EXCLUDED.language
        """,
            user_id,
            language,
        )


async def update_user_rating(user_id: int, rating: int, username: str):
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
        INSERT INTO users (user_id, user_rating, chess_username)
        VALUES ($1, $2, $3)
        ON CONFLICT (user_id) DO UPDATE SET
            user_rating = EXCLUDED.user_rating,
            chess_username = EXCLUDED.chess_username
        """,
            user_id,
            rating,
            username,
        )


async def remove_user(user_id: int):
    async with db_pool.acquire() as conn:
        await conn.execute("DELETE FROM users WHERE user_id = $1", user_id)


async def is_user_registered(user_id: int) -> bool:
    async with db_pool.acquire() as conn:
        result = await conn.fetchval("SELECT 1 FROM users WHERE user_id = $1", user_id)
        return result is not None


async def get_user_count() -> int:
    async with db_pool.acquire() as conn:
        return await conn.fetchval("SELECT COUNT(*) FROM users")


async def get_all_user_ids():
    async with db_pool.acquire() as conn:
        result = await conn.fetch("SELECT user_id FROM users")
        return [record["user_id"] for record in result]


async def get_user_language(user_id: int) -> str:
    async with db_pool.acquire() as conn:
        result = await conn.fetchval(
            "SELECT language FROM users WHERE user_id = $1", user_id
        )
        return result or "en"


async def get_user_data(user_id: int, fields=None):
    fields_str = ", ".join(fields) if fields else "*"
    async with db_pool.acquire() as conn:
        result = await conn.fetchrow(
            f"SELECT {fields_str} FROM users WHERE user_id = $1", user_id
        )
        return dict(result) if result else None


async def get_user_rating(user_id: int):
    async with db_pool.acquire() as conn:
        return await conn.fetchval(
            "SELECT user_rating FROM users WHERE user_id = $1", user_id
        )


async def get_top_players(limit=10):
    async with db_pool.acquire() as conn:
        return await conn.fetch(
            """
        SELECT user_id, chess_username, user_rating FROM users
        WHERE user_rating IS NOT NULL
        ORDER BY user_rating DESC
        LIMIT $1
        """,
            limit,
        )
