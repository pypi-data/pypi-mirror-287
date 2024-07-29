import pytest
import asyncio
from cerina import Completion

@pytest.mark.asyncio
async def test_create():
    completion = Completion()
    prompt = "Test prompt"
    response = await completion.create(prompt)
    assert isinstance(response, str)
