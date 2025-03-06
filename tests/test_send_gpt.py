import pytest
from core.bot import send_chess_fact


@pytest.mark.asyncio
async def test_send_chess_fact():
    """
    Tests if the send_chess_fact function runs without errors.
    """
    try:
        await send_chess_fact() 
    except Exception as e:
        pytest.fail(f"send_chess_fact() failed with error: {e}")
