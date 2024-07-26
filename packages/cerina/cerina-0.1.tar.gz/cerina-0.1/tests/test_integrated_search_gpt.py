import pytest
import asyncio
from cerina import IntegratedSearchGPT

@pytest.mark.asyncio
async def test_generate_with_search():
    integrated_search_gpt = IntegratedSearchGPT()
    query = "Test query"
    response = await integrated_search_gpt.generate_with_search(query)
    assert isinstance(response, str)
