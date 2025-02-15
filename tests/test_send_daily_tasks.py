import pytest
import asyncio
from core.bot import send_daily_puzzle, send_daily_chess_images

@pytest.mark.asyncio
async def test_send_daily_puzzle():
    """Test if send_daily_puzzle() runs without errors."""
    try:
        await send_daily_puzzle()
    except Exception as e:
        pytest.fail(f"send_daily_puzzle() failed with error: {e}")

@pytest.mark.asyncio
async def test_send_daily_chess_images():
    """Test if send_daily_chess_images() runs without errors."""
    try:
        await send_daily_chess_images()
    except Exception as e:
        pytest.fail(f"send_daily_chess_images() failed with error: {e}")